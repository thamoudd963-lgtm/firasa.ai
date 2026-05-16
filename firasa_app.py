
<span class="section-num">04</span>
                      <span class="section-title">نصيحة الفِراسة الذهبية</span>
                    </div>""", unsafe_allow_html=True)
                    st.markdown(f"""
                    <div class="advice-block">
                      <div class="advice-eyebrow">Golden Insight</div>
                      <div class="advice-text">{advice}</div>
                    </div>""", unsafe_allow_html=True)

                if not traits and not replies:
                    st.markdown(f'<div class="hidden-block">{text}</div>', unsafe_allow_html=True)

            except Exception as e:
                st.error(f"حدث خطأ: {e}")

# ── FOOTER ──
st.markdown("""
<div class="footer-wrap">
  <div class="footer-name">thamoud</div>
  <div class="footer-role">Developer · فِراسة AI</div>
  <a class="footer-ig" href="https://www.instagram.com/thamoudd?igsh=ZHB0bjdzbXM5dGx0" target="_blank">
    <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
      <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
    </svg>
    @thamoudd
  </a>
  <div class="footer-copy">© 2026 Firasa AI · All rights reserved</div>
</div>
""", unsafe_allow_html=True)
