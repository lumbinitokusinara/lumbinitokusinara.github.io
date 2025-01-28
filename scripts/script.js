
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
  '/images/Lumbini.jpg',
  '/images/MahabodhiTemple.jpg',
  '/images/Bodhi_Tree_Distant_View_-_panoramio.jpg',
  '/images/Vajirashila.jpg',
  '/images/Great_Buddha_Statue,_Bodh_Gaya_1024px.jpg',
  '/images/MahabodhiTemple2.jpg',
  '/images/1024px-Kusinara.jpg',
  '/images/Kusinara2.jpg',
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