import streamlit as st

# Set page config (only once at the top)
st.set_page_config(page_title="Audio Basics", page_icon="🎵")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Learn Bit Depth", "Learn Bit Rate", "Interactive Demo", "Glossary"])

# Page content based on selection
if page == "Home":
    st.title("Audio Basics")
    st.write("**Welcome Message**: Hear the difference, master your sound, and manage your storage!")
    st.write("Explore the essentials of digital audio for multi-track recording. Choose a section below to dive in.")
    st.markdown("""
    - **Learn Bit Depth**: Understand how bit depth affects audio detail and noise.  
    - **Learn Bit Rate**: Discover how bit rate and sample rate shape quality and storage.  
    - **Interactive Demo**: Try recording settings and hear the results.  
    - **Glossary**: Quick reference for key terms.
    """)

elif page == "Learn Bit Depth":
    st.title("Learn Bit Depth")
    st.write("**Definition**: Bit depth controls the detail in your audio—like shades in a painting.")

    st.subheader("Sonic Quality Differences")
    st.write("""
    - **8-bit**: Harsh, noisy, 'crunchy' sound due to quantization distortion (only 256 volume levels). Best for lo-fi effects, not pro recording.  
    - **16-bit**: Smooth, clean, with decent dynamic range (~96 dB). Standard for CDs, good for most instruments, but subtle details in quiet passages may clip or hiss.  
    - **24-bit**: Rich, detailed, with vast dynamic range (~144 dB). Captures whispers to screams without noise—ideal for pro studios, especially for vocals or acoustic instruments.
    """)

    st.subheader("Audio Examples")
    st.write("- Piano chord: 8-bit (gritty, distorted) vs. 16-bit (clean) vs. 24-bit (nuanced, airy).")
    st.write("- Vocal whisper: 16-bit (slight hiss in silence) vs. 24-bit (pristine quiet).")
    st.info("Note: Audio playback not implemented here—imagine the differences or upload your own files in the Interactive Demo!")

    st.subheader("Visual Aid")
    st.write("Picture a waveform: 'steps' (quantization) smooth out as bit depth increases from 8-bit to 24-bit.")

elif page == "Learn Bit Rate":
    st.title("Learn Bit Rate")
    st.write("**Definition**: Bit rate is the data per second—higher rates carry more sound info.")
    st.write("**Formula**: Bit Rate = Sample Rate × Bit Depth × Channels (stereo = 2 channels).")

    st.subheader("Sonic Quality Differences & Storage")
    st.write("""
    - **44.1 kHz, 16-bit (1,411 kbps)**:  
      - *Quality*: Clear for most music, but high frequencies (e.g., cymbals) may lack sparkle. Faint noise in quiet parts.  
      - *Storage*: ~10.3 MB/min.  
    - **48 kHz, 24-bit (2,304 kbps)**:  
      - *Quality*: Crisper highs than 44.1 kHz, better depth, less noise. Great for video sync.  
      - *Storage*: ~16.9 MB/min.  
    - **96 kHz, 24-bit (4,608 kbps)**:  
      - *Quality*: Ultra-clear highs (e.g., shimmering hi-hats), spacious, no noise. Perfect for strings or percussion.  
      - *Storage*: ~33.8 MB/min.  
    - **192 kHz, 24-bit (9,216 kbps)**:  
      - *Quality*: Maximum fidelity—captures every nuance (e.g., string harmonics, breath in vocals). Great for pro mixing.  
      - *Storage*: ~67.5 MB/min.
    """)

    st.subheader("Audio Examples")
    st.write("- Cymbal crash: 44.1 kHz/16-bit (dull edge) vs. 192 kHz/24-bit (crisp, extended shimmer).")
    st.write("- Acoustic guitar: 48 kHz/24-bit (warm, solid) vs. 96 kHz/24-bit (open, detailed).")
    st.info("Audio examples are descriptive—test these in the Interactive Demo!")

    st.subheader("Visual Aid")
    st.write("Imagine a 'data pipe' widening with bit rate, and a frequency graph showing more high-end detail.")
    st.write("**Analogy**: Low bit rate is a sketch—high bit rate is a full-color photo.")

elif page == "Interactive Demo":
    st.title("Interactive Demo")
    st.write("Try recording settings and hear the results—link quality to storage trade-offs.")

    st.subheader("Record & Compare")
    bit_depth = st.selectbox("Bit Depth", ["16-bit", "24-bit"])
    sample_rate = st.selectbox("Sample Rate", ["44.1 kHz", "48 kHz", "96 kHz", "192 kHz"])

    # Calculate bit rate and storage
    settings = {
        ("44.1 kHz", "16-bit"): (1411, "~1.7 MB/10s", "~10.3 MB/min", "Good clarity, but highs feel flat, faint noise in silence"),
        ("48 kHz", "24-bit"): (2304, "~2.8 MB/10s", "~16.9 MB/min", "Cleaner, with subtle high-end lift—great all-rounder"),
        ("96 kHz", "24-bit"): (4608, "~5.6 MB/10s", "~33.8 MB/min", "Crystal-clear detail, spacious sound—pro-level quality"),
        ("192 kHz", "24-bit"): (9216, "~11.3 MB/10s", "~67.5 MB/min", "Every nuance shines—top-tier fidelity, huge files")
    }
    bit_rate, mb_10s, mb_min, sonic_note = settings.get((sample_rate, bit_depth), (0, "N/A", "N/A", "N/A"))

    st.write(f"**Bit Rate**: {bit_rate} kbps")
    st.write(f"**Storage**: {mb_10s} for 10 seconds, {mb_min} per minute")
    st.write(f"**Sonic Note**: {sonic_note}")

    # Placeholder for recording
    st.write("Upload a short audio file (e.g., 10s of clapping) to simulate recording:")
    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])
    if uploaded_file:
        st.write("File uploaded! In a full app, you’d hear it processed at your settings.")
        st.write("Feedback example: 'Hear the hiss drop from 16-bit to 24-bit?'")

    st.info("Recording and playback are simulated—real audio requires additional libraries.")

elif page == "Glossary":
    st.title("Glossary")
    st.write("Quick reference for key terms:")

    st.markdown("""
    - **Bit Depth**: Number of volume levels—higher means less noise, more detail.  
    - **Bit Rate**: Data per second; higher rates mean better sound, bigger files.  
    - **Sample Rate**: How often audio is measured per second (e.g., 44.1 kHz = 44,100 times).  
    - **Dynamic Range**: Range from softest to loudest sounds—grows with bit depth.  
    - **Quantization Noise**: Distortion from low bit depth—sounds gritty.  
    - **Frequency Response**: How well highs are captured—improves with sample rate.  
    - **MB/min**: Megabytes per minute—how much storage your audio needs.
    """)

# Optional footer
st.sidebar.write("Built for musicians by Audio Basics © 2025")
