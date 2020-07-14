const grid = document.querySelector('.container__grid');
const fetchButton = document.querySelector('.button--fetch');
const loading = document.querySelector('.loading');

const request = async (url) => {
  const blob = await fetch(url);
  return blob.json();
};

const fetchImage = async () => {
  loading.classList.add('active');
  const datas = await request(
    'https://api.thecatapi.com/v1/images/search?limit=30'
  );

  grid.innerHTML = datas
    .map((data) => {
      return `
    <img src="${data.url}" />
  `;
    })
    .join('');
  loading.classList.remove('active');
};

fetchButton.addEventListener('click', fetchImage);
fetchImage();
