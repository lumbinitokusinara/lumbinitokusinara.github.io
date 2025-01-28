
// script.js
// Dropdown Navigation
const dropdown = document.getElementById('section-dropdown');
dropdown.addEventListener('change', function () {
  const selectedPage = this.value;
  if (selectedPage) {
    window.location.href = selectedPage;
  }
});

// Background Image Rotation (for homepage)
const images = [
  '/images/bodhgaya1.jpg',
  '/images/bodhgaya2.jpg',
  '/images/Lumbini.jpg',
  // Add more image paths as needed
];

let currentImageIndex = 0;
const heroSection = document.getElementById('hero-section');

function changeBackgroundImage() {
  if (heroSection) {
    currentImageIndex = (currentImageIndex + 1) % images.length;
    heroSection.style.backgroundImage = `url('${images[currentImageIndex]}')`;
  }
}

if (heroSection) {
  setInterval(changeBackgroundImage, 5000);
}

// Card Navigation (for homepage)
const cards = document.querySelectorAll('.card');
cards.forEach(card => {
  card.addEventListener('click', () => {
    const page = card.getAttribute('data-page');
    window.location.href = page;
  });
});