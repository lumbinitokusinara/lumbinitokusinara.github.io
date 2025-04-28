
// script.js



////////////////////////////////
// script.js
// Function to load content from JSON
async function loadContent() {
  const currentPage = window.location.pathname.split('/').pop().split('.')[0]; // e.g., "page1"
  const response = await fetch('/pages/content.json');
  const contentData = await response.json();

  // console.log(currentPage);
  // console.log(contentData);

  const mainElement = document.getElementById('content');
  if (contentData[currentPage]) {
    mainElement.innerHTML = contentData[currentPage]; // Render HTML content
  } else {
    mainElement.innerHTML = '<p>Content not found.</p>';
  }
}

// Load content when the page loads
window.onload = loadContent;

// Dropdown Navigation
const dropdown = document.getElementById('section-dropdown');
if (dropdown) {
  dropdown.addEventListener('change', function () {
    const selectedPage = this.value;
    if (selectedPage) {
      window.location.href = selectedPage;
    }
  });
}


const dropdown2 = document.getElementById('section-dropdown2');
if (dropdown2) {
    console.log("dropdown2 -----");
    console.log(dropdown2);
    dropdown2.addEventListener('change', function () {
    const selectedPage2 = this.value;
    console.log(selectedPage2);
    if (selectedPage2) {
      window.location.href = selectedPage2;
    }
  });
}

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


// Dynamic Next and Previous Links
const currentPage = window.location.pathname.split('/').pop(); // Get current page filename
const pages = [
  'page1.html',
  'page2.html',
  'page3.html',
  'page4.html',
  'page4_1.html',
  'page5.html',
  'page6.html',
  'page7.html',
  'page8.html',
  'page9.html',
  'page10.html',
  'page11_1.html',
  'page11_2.html',
  'page12.html',
  'page13.html',
  'page13_1.html',
  'page13_2.html',
  'page14_1.html',
  'page14_2.html',
  'page14_3.html',
  'page15_1.html',
  'page15_2.html',
  'page15_3.html',
  'page15_4.html',
  'page16_1.html',
  'page16_2.html',
  'page16_3.html',
  'page17.html',
  'page18.html',
  'page19_1.html',
  'page19_2.html',
  'page19_3.html',
  'page19_4.html',
  'page19_5.html',
  // Add more pages as needed
];

const currentIndex = pages.indexOf(currentPage);

console.log(currentPage);
console.log(currentIndex);

if (currentIndex !== -1) {
  const navButtons = document.createElement('div');
  navButtons.className = 'nav-buttons';

  if (currentIndex > 0) {
    const previousButton = document.createElement('a');
    previousButton.href = pages[currentIndex - 1];
    previousButton.className = 'previous-button';
    previousButton.textContent = '← Previous';
    navButtons.appendChild(previousButton);
  }

  if (currentIndex < pages.length - 1) {
    const nextButton = document.createElement('a');
    nextButton.href = pages[currentIndex + 1];
    nextButton.className = 'next-button';
    nextButton.textContent = 'Next →';
    navButtons.appendChild(nextButton);
  }

  document.body.appendChild(navButtons);
}
