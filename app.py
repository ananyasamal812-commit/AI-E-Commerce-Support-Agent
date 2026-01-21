import streamlit as st
from rag import rag_pipeline

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI E-Commerce Support Agent",
    page_icon="🛒",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
    color: #111;
}

.product-row {
    background: white;
    border-radius: 14px;
    padding: 14px 18px;
    margin-bottom: 14px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    gap: 14px;
}

.product-icon {
    font-size: 34px;
}

.product-name {
    font-size: 17px;
    font-weight: 600;
}

.product-desc {
    font-size: 13px;
    color: #555;
}

.product-price {
    font-size: 15px;
    font-weight: 700;
    color: #0f9d58;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def category_icon(category):
    icons = {
        "television": "📺",
        "smartphone": "📱",
        "laptop": "💻",
        "headphone": "🎧",
        "smartwatch": "⌚"
    }
    return icons.get(category.lower(), "🛍️")




# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🛒 AI E-Commerce Support Agent")
st.caption("Retrieval Based • No Hallucination • Clean UI")

# --------------------------------------------------
# USER INPUT
# --------------------------------------------------
query = st.chat_input("Ask for products (e.g. 'phone under 30000')")

if not query:
    st.stop()

products = rag_pipeline(query)

if not products:
    st.warning("❌ No matching products found")
    st.stop()

# --------------------------------------------------
# COMPARISON MODE
# --------------------------------------------------
if "compare" in query.lower():
    if len(products) < 2:
        st.info("Need at least 2 products to compare")
        st.stop()

    st.subheader("🔍 Product Comparison")
    col1, col2 = st.columns(2)

    for col, p in zip([col1, col2], products[:2]):
        
        col.markdown(f"### {p['name']}")
        col.write(p["description"])
        col.write(f"💰 ₹ {p['price']}")
        col.write(f"{category_icon(p['category'])} {p['category']}")

    st.stop()

# --------------------------------------------------
# PRODUCT LISTING
# --------------------------------------------------
for p in products:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    
    st.markdown(f"<div class='product-title'>{p['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='product-desc'>{p['description']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='product-price'>₹ {p['price']}</div>", unsafe_allow_html=True)
    st.markdown(f"{category_icon(p['category'])} {p['category']}")
    st.markdown("</div>", unsafe_allow_html=True)

    
