const fetchImg = document.querySelector('#fetch');
fetch('https://api.thecatapi.com/v1/images/search?size=full')
  .then((blob) => {
    if (blob.status === 200) {
      console.log('status :', 200);
      return blob.json();
    } else {
      console.log('실패..');
      return;
    }
  })
  .then((res) => {
    fetchImg.src = res[0].url;
  })
  .finally(() => {
    console.log('요청완료!');
  });

// async로 전환하기.
const request = async (url) => {
  try {
    const blob = await fetch(url);
    const { status, ok } = blob;
    if (status === 200) {
      return blob.json();
    } else if (status === 404) {
      throw new Error('찾을 수 없는 경로');
    }
  } catch (e) {
    console.log(e);
  } finally {
    console.log('이것도 완료!');
  }
};

// 이런식으로 API를 묶을 수 있다.
const api = {
  getRandomCat: () =>
    request('https://api.thecatapi.com/v1/images/search?size=full'),
};

const asyncFetchImg = document.querySelector('#asyncFetch');
// async함수는 뭐가 됐던간에 Promise를 리턴한다.
api.getRandomCat().then((data) => {
  asyncFetchImg.src = data[0].url;
});
