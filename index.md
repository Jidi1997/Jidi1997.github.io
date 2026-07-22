---
layout: about
title: home
subtitle: Ph.D. Candidate @ Sichuan University

profile:
  align: right
  image: gemini_edhec_pic.png

  image_circular: true # set to true for circular profile pic
  more_info: >
    <p>Business School, Sichuan University</p>
    <p>Chengdu, China</p>

announcements:
  enabled: false # includes a list of news items
  scrollable: true # set to true for a scrollable list
  limit: 5 # max number of news items to display

latest_posts:
  enabled: false # includes a list of the newest posts

social: true # includes social icons at the bottom of the page
---

<div class="glass-card" markdown="1">
### Bio
👋 Welcome! I am a Ph.D. Candidate in Finance at Sichuan University. I am on the 2026/2027 academic job market and available for interviews ([My CV]({{ '/assets/pdf/2607_Jidi_CV.pdf' | relative_url }})).

🌏 My research interests are corporate governance and sustainability, and I'm enthusiastic about large language models, text analysis, and agentic AI and their use in research (see my [personal projects](/repositories/)). 

🇩🇪 I was sponsored by the China Scholarship Council (CSC) as a visiting Ph.D student in Finance at TUM School of Management, Technical University of Munich, Germany (2023–2024), under the supervision of Prof. Sebastian Müller, CFA. 

🇫🇷 🇱🇺 Prior to conducting academic research, I earned a Master's degree in Accounting and Finance from EDHEC Business School in France (2021), and worked as a financial analyst at PingPong Payment S.A. in Luxembourg (2021).
</div>

<div class="glass-card" markdown="1">
### Research Interests
*   Shareholder activism
*   Corporate governance
*   Sustainable finance and climate change
</div>  

<div class="glass-card" markdown="1">
### Working Papers

**[Silencing the Green Engine: How Shareholder Voice Suppresses Innovation](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6944718)** (_Job market paper_)  

<div class="custom-audio-wrapper">
  <div class="custom-audio-label">
    <strong>🎧 2-min audio overview:</strong>
  </div>
  <div class="custom-audio-player">
    <audio id="jmp-audio" preload="metadata">
      <source src="{{ '/assets/audio/26-2min-audio.m4a' | relative_url }}" type="audio/mp4">
      Your browser does not support the audio element.
    </audio>
    
    <button class="player-btn play-btn" id="jmp-play-btn" aria-label="Play">
      <!-- Play icon -->
      <svg class="play-icon" viewBox="0 0 24 24">
        <path d="M8 5v14l11-7z"/>
      </svg>
      <!-- Pause icon -->
      <svg class="pause-icon" viewBox="0 0 24 24" style="display: none;">
        <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
      </svg>
    </button>
    
    <div class="player-timeline-container">
      <input type="range" class="player-slider" id="jmp-progress" min="0" max="100" value="0">
      <div class="player-time-display">
        <span id="jmp-current-time">0:00</span>
        <span>/</span>
        <span id="jmp-duration">0:00</span>
      </div>
    </div>
    
    <div class="player-actions">
      <button class="player-speed-badge" id="jmp-speed-btn" title="Playback speed">1.0x</button>
      <button class="player-btn mute-btn" id="jmp-mute-btn" aria-label="Mute">
        <!-- Volume SVG -->
        <svg class="volume-icon" viewBox="0 0 24 24">
          <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
        </svg>
        <!-- Mute SVG (hidden) -->
        <svg class="mute-icon" viewBox="0 0 24 24" style="display: none;">
          <path d="M16.5 12c0-1.77-1.02-3.29-2.5-4.03v2.21l2.45 2.45c.03-.21.05-.42.05-.63zm2.5 0c0 .94-.2 1.82-.54 2.64l1.51 1.51C20.63 14.91 21 13.5 21 12c0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zM4.27 3L3 4.27 7.73 9H3v6h4l5 5v-6.73l4.25 4.25c-.67.52-1.42.93-2.25 1.18v2.06c1.38-.31 2.63-.95 3.69-1.81L19.73 21 21 19.73l-9-9L4.27 3zM12 4L9.91 6.09 12 8.18V4z"/>
        </svg>
      </button>
    </div>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  const audio = document.getElementById("jmp-audio");
  const playBtn = document.getElementById("jmp-play-btn");
  const playIcon = playBtn.querySelector(".play-icon");
  const pauseIcon = playBtn.querySelector(".pause-icon");
  const progressBar = document.getElementById("jmp-progress");
  const currentTimeEl = document.getElementById("jmp-current-time");
  const durationEl = document.getElementById("jmp-duration");
  const speedBtn = document.getElementById("jmp-speed-btn");
  const muteBtn = document.getElementById("jmp-mute-btn");
  const volumeIcon = muteBtn.querySelector(".volume-icon");
  const muteIcon = muteBtn.querySelector(".mute-icon");

  function formatTime(secs) {
    if (isNaN(secs)) return "0:00";
    const minutes = Math.floor(secs / 60);
    const seconds = Math.floor(secs % 60);
    return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
  }

  function updateProgressStyle() {
    const val = progressBar.value;
    const min = progressBar.min ? progressBar.min : 0;
    const max = progressBar.max ? progressBar.max : 100;
    const percentage = ((val - min) / (max - min)) * 100;
    
    const activeColor = getComputedStyle(document.documentElement)
      .getPropertyValue('--global-theme-color').trim() || '#800080';
    const trackColor = getComputedStyle(document.documentElement)
      .getPropertyValue('--global-divider-color').trim() || '#e0e0e0';
      
    progressBar.style.background = `linear-gradient(to right, ${activeColor} 0%, ${activeColor} ${percentage}%, ${trackColor} ${percentage}%, ${trackColor} 100%)`;
  }

  audio.addEventListener("loadedmetadata", function() {
    durationEl.textContent = formatTime(audio.duration);
    progressBar.max = Math.floor(audio.duration);
    updateProgressStyle();
  });

  audio.addEventListener("timeupdate", function() {
    if (!progressBar.classList.contains("dragging")) {
      progressBar.value = Math.floor(audio.currentTime);
      currentTimeEl.textContent = formatTime(audio.currentTime);
      updateProgressStyle();
    }
  });

  playBtn.addEventListener("click", function() {
    if (audio.paused) {
      audio.play().catch(err => console.log("Audio playback failed: ", err));
      playIcon.style.display = "none";
      pauseIcon.style.display = "block";
    } else {
      audio.pause();
      playIcon.style.display = "block";
      pauseIcon.style.display = "none";
    }
  });

  progressBar.addEventListener("mousedown", () => progressBar.classList.add("dragging"));
  progressBar.addEventListener("touchstart", () => progressBar.classList.add("dragging"));

  progressBar.addEventListener("input", function() {
    currentTimeEl.textContent = formatTime(progressBar.value);
    updateProgressStyle();
  });

  progressBar.addEventListener("change", function() {
    audio.currentTime = progressBar.value;
    progressBar.classList.remove("dragging");
  });

  progressBar.addEventListener("mouseup", () => progressBar.classList.remove("dragging"));
  progressBar.addEventListener("touchend", () => progressBar.classList.remove("dragging"));

  const speeds = [1.0, 1.25, 1.5, 2.0];
  let currentSpeedIdx = 0;
  speedBtn.addEventListener("click", function() {
    currentSpeedIdx = (currentSpeedIdx + 1) % speeds.length;
    const newSpeed = speeds[currentSpeedIdx];
    audio.playbackRate = newSpeed;
    speedBtn.textContent = `${newSpeed.toFixed(2).replace(/\.00$/, '')}x`;
  });

  muteBtn.addEventListener("click", function() {
    audio.muted = !audio.muted;
    if (audio.muted) {
      volumeIcon.style.display = "none";
      muteIcon.style.display = "block";
    } else {
      volumeIcon.style.display = "block";
      muteIcon.style.display = "none";
    }
  });

  audio.addEventListener("ended", function() {
    playIcon.style.display = "block";
    pauseIcon.style.display = "none";
    progressBar.value = 0;
    currentTimeEl.textContent = "0:00";
    updateProgressStyle();
  });

  // Watch for theme changes to adapt layout
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.attributeName === 'data-theme') {
        updateProgressStyle();
      }
    });
  });
  observer.observe(document.documentElement, { attributes: true });

  if (audio.readyState >= 1) {
    durationEl.textContent = formatTime(audio.duration);
    progressBar.max = Math.floor(audio.duration);
    updateProgressStyle();
  }
});
</script>

Using a large language model to classify environmental shareholder proposals, we find that proposals advancing to a public vote significantly suppress green innovation.
Evidence from media coverage and executive compensation is consistent with a multitasking mechanism in which activism increases short-term reputational pressures while weakening incentives for long-horizon investment. 
However, public activism successfully promotes green innovation for firms with ex ante environmental deficiencies, during periods of heightened climate sentiment, or when sponsored by insititutional investors.   
Our findings highlight an unintended friction of public ESG engagement in the absence of informed target selection and timing. 

👉[Fine-tuned LLM and trainingset used are available on Hugging Face](https://huggingface.co/Jidi1997/ClimateBERT_GPROP_Detector)

---

**Words of (No-) Action: Regulatory Discretion and Shareholder Voice** (_Work in progress_)  
With Christian Breitung and Sebastian Müller

Using the setting of SEC Rule 14a-8, we construct a dataset of over 5,300 SEC no-action letters that captures the complete life cycle of management-contested shareholder proposals.We study a selection problem in shareholder proposal disputes, examining the economic trade-offs underlying the SEC's allocation of review effort under capacity constraints within the Rule 14a-8 regime. We develop a retrieval-based architecture and machine learning model to process unstructured correspondence in this multi-party bargaining setting of corporate governance. We aim to provide evidence on how SEC regulatory screening shapes shareholder "voice" and at what cost, with implications for the ongoing policy debate over Rule 14a-8.
</div>


<div class="glass-card" markdown="1">
### Workshops and Conferences
* Workshop on Corporate Governance in the Era of Climate Change (Guest speaker: Roni Michaely, University of Hong Kong), Sichuan University, co-organizer (Est. 2026, Chengdu, China)
* Swedish House of Finance and ECGI Annual Conference on Corporate Governance, participant (August 27–28, 2024, Stockholm, Sweden)
* The 2nd European Sustainable Finance Ph.D. Workshop, participant (June 18–29, 2024, Augsburg, Germany)
* ESG Risk Management Framework for the Financial Sector, participant (May 29, 2024, Vienna, Austria)
* Workshop on Current Research Trends in Sustainable Finance, poster presenter (November 16–17, 2023, Heilbronn, Germany)
</div>  