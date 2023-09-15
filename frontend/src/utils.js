export function getRandomColor() {
  return "#" + ((Math.random() * 0xffffff) << 0).toString(16);
}
export function getTextWidth(ref) {
  return ref.value.getBoundingClientRect().width;
}
export function setBackground(ref, color) {
  ref.value.style.backgroundColor = color;
}
