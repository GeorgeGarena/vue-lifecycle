<template>
  <div>
    <h3>Children component</h3>
    <span ref="sumRef" id="sum">{{ myCount + count }}</span>
    <button @click="myCount += 1">myCount: {{ myCount }}</button>
  </div>
</template>
<script setup>
import {
  ref,
  onBeforeMount,
  onMounted,
  onBeforeUpdate,
  onUpdated,
  onBeforeUnmount,
  onUnmounted,
} from "vue";
console.log("%cChildren component setup", "color: skyblue");
const props = defineProps({
  count: Number,
});
const myCount = ref(0);
const sumRef = ref(null);

onBeforeMount(() => {
  console.log("%conBeforeMount", "color: skyblue");
  console.log(`--sumRef.value: ${sumRef.value}`);
});
onMounted(() => {
  console.log("%conMounted", "color: skyblue");
  console.log("--sumRef.value.innerHTML", sumRef.value.innerHTML);
});
onBeforeUpdate(() => {
  console.log("%conBeforeUpdate", "color: skyblue");
  console.log("--sumRef.value.innerHTML", sumRef.value.innerHTML);
});
onUpdated(() => {
  console.log("%conUpdate", "color: skyblue");
  console.log("--sumRef.value.innerHTML", sumRef.value.innerHTML);
});
onBeforeUnmount(() => {
  console.log("%conBeforeUnmount", "color: skyblue");
});
onUnmounted(() => {
  console.log("%conUnmounted", "color: skyblue");
});
</script>
