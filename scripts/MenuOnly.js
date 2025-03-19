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