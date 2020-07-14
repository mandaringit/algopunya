// 위크맵과 그 위크맵을 사용하는 클래스를 함께 IIFE에 넣었다.
const SecretHolder = (function () {
  const secrets = new WeakMap();
  return class {
    setSecret(secret) {
      secrets.set(this, secret) // 키가 this, value가 secret.
    }
    getSecret(){
      return secrets.get(this)
    }
  }
})();

const a = new SecretHolder();
const b = new SecretHolder();

// 저장시 setSecret을 써야만하고
a.setSecret('secret A');
b.setSecret('secret B');

// 보려할땐 getSecret을 써야만 함
console.log(a.getSecret());
console.log(b.getSecret());