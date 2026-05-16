import streamlit as st
import google.generativeai as genai
import re

# ── Page config ──
st.set_page_config(
    page_title="فِراسة AI",
    page_icon="👁️",
    layout="centered"
)

# ── CSS: أبيض وأسود فاخر ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Amiri:wght@400;700&family=Courier+Prime:wght@400;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #f5f5f3 !important;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stMain"] { background: #f5f5f3 !important; }

/* Hero */
.hero {
    background: #111111;
    padding: 52px 24px 44px;
    text-align: center;
    margin: -1rem -1rem 2rem -1rem;
}
.hero-badge {
    font-family: 'Courier Prime', monospace;
    font-size: 10px; letter-spacing: 5px;
    color: #555; text-transform: uppercase; margin-bottom: 20px;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 64px; font-weight: 700;
    color: #ffffff; letter-spacing: -2px;
    line-height: 1; margin: 12px 0 8px;
}
.hero-title span { color: #555; font-style: italic; font-weight: 400; }
.hero-line {
    width: 32px; height: 1px;
    background: #333; margin: 18px auto;
}
.hero-sub {
    font-family: 'Amiri', serif;
    font-size: 16px; color: #666; direction: rtl;
}

/* Input card */
.input-label {
    font-family: 'Courier Prime', monospace;
    font-size: 10px; letter-spacing: 3px;
    color: #999; text-transform: uppercase;
    text-align: right; margin-bottom: 6px;
}
[data-testid="stTextArea"] textarea {
    background: #ffffff !important;
    color: #111111 !important;
    font-family: 'Amiri', serif !important;
    font-size: 16px !important;
    line-height: 1.9 !important;
    border: 1px solid #e2e2e2 !important;
    border-radius: 0 !important;
    direction: rtl;
    text-align: right;
    padding: 16px !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: #111 !important;
    box-shadow: none !important;
}

/* Button */
[data-testid="stButton"] > button {
    width: 100% !important;
    background: #111111 !important;
    color: #ffffff !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 0 !important;
    padding: 18px !important;
    letter-spacing: 0.5px !important;
    transition: background 0.2s !important;
}
[data-testid="stButton"] > button:hover {
    background: #1a1a1a !important;
}

/* Section headers */
.sec-header {
    display: flex; align-items: center; gap: 12px;
    direction: rtl; border-bottom: 2px solid #111;
    padding-bottom: 12px; margin: 32px 0 20px;
}
.sec-num {
    font-family: 'Courier Prime', monospace;
    font-size: 10px; color: #bbb; letter-spacing: 2px;
    border: 1px solid #ddd; padding: 2px 8px;
}
.sec-title {
    font-family: 'Playfair Display', serif;
    font-size: 18px; font-weight: 700; color: #111;
}

/* Percent bar */
.bar-wrap { margin-bottom: 16px; }
.bar-label-row {
    display: flex; justify-content: space-between;
    direction: rtl; margin-bottom: 6px;
}
.bar-label {
    font-family: 'Amiri', serif;
    font-size: 15px; color: #111; font-weight: 700;
}
.bar-val {
    font-family: 'Courier Prime', monospace;
    font-size: 12px; color: #111; font-weight: 700;
}
.bar-track {
    height: 4px; background: #ebebeb;
}
.bar-fill {
    height: 4px; background: #111;
    transition: width 0.3s;
}

/* Hidden block */
.hidden-block {
    background: #ffffff;
    border-right: 3px solid #111;
    padding: 20px 24px;
    font-family: 'Amiri', serif;
    font-size: 15.5px; line-height: 2;
    color: #333; direction: rtl; text-align: right;
}

/* Reply cards */
.reply-card {
    border: 1.5px solid #e8e8e8;
    padding: 20px 24px; margin-bottom: 12px;
    background: white;
}
.reply-card-dark {
    border: 1.5px solid #111;
    padding: 20px 24px; margin-bottom: 12px;
    background: #111;
}
.reply-type {
    font-family: 'Courier Prime', monospace;
    font-size: 10px; letter-spacing: 3px;
    color: #999; text-transform: uppercase; margin-bottom: 10px;
    text-align: right; direction: rtl;
}
.reply-type-dark {
    font-family: 'Courier Prime', monospace;
    font-size: 10px; letter-spacing: 3px;
    color: #555; text-transform: uppercase; margin-bottom: 10px;
    text-align: right; direction: rtl;
}
.reply-text {
    font-family: 'Amiri', serif;
    font-size: 15.5px; line-height: 1.95;
    color: #333; direction: rtl; text-align: right;
}
.reply-text-dark {
    font-family: 'Amiri', serif;
    font-size: 15.5px; line-height: 1.95;
    color: #ccc; direction: rtl; text-align: right;
}

/* Advice block */
.advice-block {
    background: #111; padding: 32px;
    direction: rtl; text-align: right;
}
.advice-badge {
    font-family: 'Courier Prime', monospace;
    font-size: 9px; letter-spacing: 4px;
    color: #555; margin-bottom: 14px;
    text-transform: uppercase;
}
.advice-text {
    font-family: 'Playfair Display', serif;
    font-size: 16px; font-style: italic;
    color: #ccc; line-height: 2;
}

/* Result header */
.result-header {
    display: flex; justify-content: space-between;
    align-items: center; direction: rtl;
    border-bottom: 2px solid #111;
    padding-bottom: 16px; margin-bottom: 36px;
}
.result-title {
    font-family: 'Playfair Display', serif;
    font-size: 22px; font-weight: 700; color: #111;
}
.result-badge {
    font-family: 'Courier Prime', monospace;
    font-size: 9px; letter-spacing: 3px;
    color: white; background: #111; padding: 5px 12px;
}

/* footer */
.footer {
    text-align: center; margin-top: 60px;
    font-family: 'Courier Prime', monospace;
    font-size: 10px; letter-spacing: 3px; color: #ccc;
}

/* hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──
st.markdown("""
<div class="hero">
  <p class="hero-badge">Digital Physiognomy Engine · v2.0</p>
  <svg width="80" height="50" viewBox="0 0 100 62" fill="none" style="margin-bottom:12px">
    <path d="M5 31 Q50 -8 95 31 Q50 70 5 31Z" stroke="white" stroke-width="2" fill="none"/>
    <circle cx="50" cy="31" r="15" fill="white" opacity="0.1"/>
    <circle cx="50" cy="31" r="10" stroke="white" stroke-width="1.5" fill="none"/>
    <circle cx="50" cy="31" r="4" fill="white"/>
    <circle cx="54" cy="27" r="2" fill="white" opacity="0.5"/>
  </svg>
  <div class="hero-title">فِراسة <span>AI</span></div>
  <div class="hero-line"></div>
  <p class="hero-sub">حلّل الشخصيات · اقرأ ما بين السطور · تصرّف بذكاء استراتيجي</p>
</div>
""", unsafe_allow_html=True)

# ── API Key ──
try:
    api_key = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("⚠ لم يتم العثور على مفتاح API في الـ Secrets.")
    st.stop()

model = genai.GenerativeModel('gemini-1.5-flash')
# ── Input ──
st.markdown('<p class="input-label">النص المراد تحليله</p>', unsafe_allow_html=True)
user_input = st.text_area(
    label="النص",
    height=160,
    placeholder="الصق هنا رسالة، مقال، أو أي نص تودّ كشف أبعاده الخفية...",
    label_visibility="collapsed"
)

if st.button("ابدأ تحليل الفِراسة ←"):
    if not user_input.strip():
        st.warning("يرجى إدخال نص للتحليل.")
    else:
        with st.spinner("جاري التحليل..."):
            prompt = f"""أنت الآن "كبير خبراء الفِراسة الرقمية". مهمتك هي تحليل النص التالي بعمق استراتيجي وتقديم تقرير مفصل يشمل:

1. **تحليل السمات بنسب مئوية**:
   - الصدق والشفافية: [X]%
   - الثقة بالنفس: [X]%
   - التوتر أو القلق: [X]%
   - العاطفية مقابل العقلانية: [X]%

2. **قراءة ما بين السطور**:
   - ما هو الهدف الحقيقي غير المعلن للكاتب من هذا النص؟
   - هل هناك نبرة تلاعب، استعطاف، أو فرض سيطرة؟

3. **اقتراحات الرد الذكي (3 خيارات)**:
   - **الرد الدبلوماسي**: لامتصاص الموقف والحفاظ على العلاقة.
   - **الرد الحازم**: لوضع حدود واضحة وإظهار القوة.
   - **الرد الودي**: إذا كان النص يحمل نوايا طيبة ويحتاج تقارباً.

4. **نصيحة "الفِراسة" الذهبية**:
   - كيف يجب أن تتعامل مع هذه الشخصية مستقبلاً بناءً على هذا النص؟

اجعل أسلوبك فخماً، تقنياً، ومفيداً جداً.

النص المطلوب تحليله:
"{user_input}"
"""
            try:
                response = model.generate_content(prompt)
                text = response.text

                # ── Parse ──
                def extract_pct(t):
                    items = []
                    for m in re.finditer(r'([^:\n*]+):\s*(\d+)%', t):
                        label = re.sub(r'[\*\-\d\.]', '', m.group(1)).strip()
                        val = int(m.group(2))
                        if 2 < len(label) < 60 and 0 <= val <= 100:
                            items.append((label, val))
                    return items

                traits = extract_pct(text)

                hidden_m = re.search(r'قراءة ما بين السطور[\s\S]*?(?=\n\d\s*[\.\-]|\*\*\d|اقتراح|$)', text, re.I)
                hidden = hidden_m.group(0).replace('**','').strip()[:600] if hidden_m else ""

                dip_m  = re.search(r'الرد الدبلوماسي[^:]*:([\s\S]*?)(?=الرد الحازم|$)', text, re.I)
                firm_m = re.search(r'الرد الحازم[^:]*:([\s\S]*?)(?=الرد الودي|$)', text, re.I)
                frnd_m = re.search(r'الرد الودي[^:]*:([\s\S]*?)(?=نصيحة|###|\d\s*\.|$)', text, re.I)
                replies = []
                if dip_m:  replies.append(("🤝 دبلوماسي", dip_m.group(1).replace('**','').strip()[:320], "light"))
                if firm_m: replies.append(("⚡ حازم",      firm_m.group(1).replace('**','').strip()[:320], "dark"))
                if frnd_m: replies.append(("✨ ودّي",      frnd_m.group(1).replace('**','').strip()[:320], "light"))

                adv_m = re.search(r'نصيحة[\s\S]*?الذهبية[^:]*:([\s\S]*?)(?=$|\n\n\n)', text, re.I)
                advice = adv_m.group(1).replace('**','').strip()[:500] if adv_m else ""

                # ── Render ──
                st.markdown("""
                <div class="result-header">
                  <span class="result-title">تقرير الفِراسة</span>
                  <span class="result-badge">CLASSIFIED</span>
                </div>""", unsafe_allow_html=True)

                # 01 traits
                if traits:
                    st.markdown("""<div class="sec-header">
                      <span class="sec-num">01</span>
                      <span class="sec-title">السمات الشخصية بالنسب المئوية</span>
                    </div>""", unsafe_allow_html=True)
                    for label, val in traits:
                        st.markdown(f"""
                        <div class="bar-wrap">
                          <div class="bar-label-row">
                            <span class="bar-label">{label}</span>
                            <span class="bar-val">{val}%</span>
                          </div>
                          <div class="bar-track">
                            <div class="bar-fill" style="width:{val}%"></div>
                          </div>
                        </div>""", unsafe_allow_html=True)

                # 02 hidden
                if hidden:
                    st.markdown("""<div class="sec-header">
                      <span class="sec-num">02</span>
                      <span class="sec-title">قراءة ما بين السطور</span>
                    </div>""", unsafe_allow_html=True)
                    st.markdown(f'<div class="hidden-block">{hidden}</div>', unsafe_allow_html=True)

                # 03 replies
                if replies:
                    st.markdown("""<div class="sec-header">
                      <span class="sec-num">03</span>
                      <span class="sec-title">اقتراحات الرد الذكي</span>
                    </div>""", unsafe_allow_html=True)
                    for rtype, rcontent, rvar in replies:
                        if rvar == "dark":
                            st.markdown(f"""
                            <div class="reply-card-dark">
                              <div class="reply-type-dark">{rtype}</div>
                              <div class="reply-text-dark">{rcontent}</div>
                            </div>""", unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div class="reply-card">
                              <div class="reply-type">{rtype}</div>
                              <div class="reply-text">{rcontent}</div>
                            </div>""", unsafe_allow_html=True)

                # 04 advice
                if advice:
                    st.markdown("""<div class="sec-header">
                      <span class="sec-num">04</span>
                      <span class="sec-title">نصيحة "الفِراسة" الذهبية</span>
                    </div>""", unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="advice-block">
                      <div class="advice-badge">GOLDEN INSIGHT</div>
                      <div class="advice-text">{advice}</div>
                    </div>""", unsafe_allow_html=True)

                # fallback
                if not traits and not replies:
                    st.markdown(f'<div class="hidden-block">{text}</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"حدث خطأ: {e}")

st.markdown('<div class="footer">FIRASA · كبير خبراء الفِراسة الرقمية</div>', unsafe_allow_html=True)
