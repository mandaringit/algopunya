const solution = require('./solution');

describe('다트게임', () => {
  it('올바른 값을 리턴한다', () => {
    expect(solution('1S2D*3T')).toBe(37);
  });
  it('올바른 값을 리턴한다', () => {
    expect(solution('1D2S#10S')).toBe(9);
  });
  it('올바른 값을 리턴한다', () => {
    expect(solution('1D2S0T')).toBe(3);
  });
  it('올바른 값을 리턴한다', () => {
    expect(solution('1S*2T*3S')).toBe(23);
  });
  it('올바른 값을 리턴한다', () => {
    expect(solution('1D#2S*3S')).toBe(5);
  });
  it('올바른 값을 리턴한다', () => {
    expect(solution('1T2D3D#')).toBe(-4);
  });
  it('올바른 값을 리턴한다', () => {
    expect(solution('1D2S3T*')).toBe(59);
  })
});