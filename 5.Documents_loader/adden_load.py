import streamlit as st
import time
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Streamlit page configuration
st.set_page_config(
    page_title="Webpage Summarizer",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .summary-box {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin-top: 1rem;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #28a745;
    }
    .error-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 5px;
        border-left: 5px solid #dc3545;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🌐 Webpage Summarizer</h1>', unsafe_allow_html=True)
st.markdown("### Extract and summarize content from any webpage")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # URL input
    default_url = "https://learnenglish.britishcouncil.org/grammar/english-grammar-reference"
    url = st.text_input("Enter Website URL:", value=default_url)
    
    # Model configuration
    st.subheader("Model Settings")
    temperature = st.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.7, step=0.1)
    
    # Summary length
    summary_length = st.selectbox(
        "Summary Length:",
        ["Brief", "Detailed", "Comprehensive"]
    )
    
    # Additional options
    include_key_points = st.checkbox("Include Key Points", value=True)
    
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("""
    1. Enter a valid website URL
    2. Adjust model settings if needed
    3. Click 'Generate Summary'
    4. View the results below
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📄 Webpage Content")
    
    if st.button("🚀 Generate Summary", type="primary", use_container_width=True):
        if not url:
            st.error("❌ Please enter a valid URL")
        else:
            try:
                # Show loading spinner
                with st.spinner("🔄 Loading webpage content..."):
                    # Load webpage
                    loader = WebBaseLoader(url)
                    docs = loader.load()
                
                if not docs or len(docs) == 0:
                    st.error("❌ No content found on the webpage")
                else:
                    # Show success message
                    st.markdown(f'<div class="success-box">✅ Successfully loaded webpage content ({len(docs)} documents)</div>', unsafe_allow_html=True)
                    
                    # Display original content in expander
                    with st.expander("📖 View Original Content (First 1000 characters)"):
                        content_preview = docs[0].page_content[:1000] + "..." if len(docs[0].page_content) > 1000 else docs[0].page_content
                        st.text_area("Content", content_preview, height=200, label_visibility="collapsed")
                    
                    # Generate summary
                    with st.spinner("🤖 Generating summary..."):
                        # Configure prompt based on user selection
                        length_map = {
                            "Brief": "Provide a concise 2-3 sentence summary",
                            "Detailed": "Provide a detailed paragraph summary",
                            "Comprehensive": "Provide a comprehensive summary with main sections"
                        }
                        
                        template = f'''
                        {length_map[summary_length]} of the following webpage content.
                        
                        Webpage Content:
                        {{webpage_content}}
                        
                        { "Also extract 3-5 key bullet points." if include_key_points else "" }
                        
                        Please provide a clear, well-structured summary:
                        '''
                        
                        prompt = PromptTemplate(
                            template=template,
                            input_variables=['webpage_content']
                        )
                        
                        model = ChatOpenAI(
                            model="deepseek/deepseek-r1-0528:free",
                            base_url="https://openrouter.ai/api/v1",
                            temperature=temperature
                        )
                        
                        parser = StrOutputParser()
                        chain = prompt | model | parser
                        
                        # Add artificial delay for better UX
                        time.sleep(1)
                        
                        summary = chain.invoke({'webpage_content': docs[0].page_content})
                    
                    # Display summary
                    st.subheader("📋 Generated Summary")
                    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
                    st.markdown(summary)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Download button for summary
                    st.download_button(
                        label="📥 Download Summary",
                        data=summary,
                        file_name=f"webpage_summary_{url.split('//')[-1].replace('/', '_')}.txt",
                        mime="text/plain"
                    )
            
            except Exception as e:
                st.markdown(f'<div class="error-box">❌ Error: {str(e)}</div>', unsafe_allow_html=True)
                st.error("Please check the URL and try again.")

with col2:
    st.subheader("ℹ️ About")
    st.markdown("""
    This tool uses AI to:
    
    - 📚 Extract content from webpages
    - 🤖 Analyze with DeepSeek model
    - 📝 Generate concise summaries
    - 🔍 Identify key information
    
    **Supported Content:**
    - Blog posts
    - Articles
    - Documentation
    - Product pages
    - News websites
    """)
    
    st.markdown("---")
    st.subheader("📊 Stats")
    if 'docs' in locals():
        st.metric("Content Length", f"{len(docs[0].page_content)} characters")
        st.metric("Documents Loaded", len(docs))
    else:
        st.metric("Content Length", "N/A")
        st.metric("Documents Loaded", "0")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Powered by LangChain • Streamlit • DeepSeek AI"
    "</div>",
    unsafe_allow_html=True
)