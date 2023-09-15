<template>
  <div>
    <h2>Lifecycle logs</h2>
    <button @click="count += 1" ref="countRef">count: {{ count }}</button>
    <ChildrenComp :count="0" />
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
import ChildrenComp from "./ChildrenComp.vue";
console.log("Lifecycle logs setup");
const count = ref(0);
const countRef = ref(null);

onBeforeMount(() => {
  console.log("%conBeforeMount", "color: orange");
  // console.log(`--countRef.value: ${countRef.value}`);
  // console.log(`--count.value: ${count.value}`);
});
onMounted(() => {
  console.log("%conMounted", "color: orange");
  // console.log(`--countRef.value: ${countRef.value.innerHTML}`);
  // console.log(`--count.value: ${count.value}`);
});
onBeforeUpdate(() => {
  console.log("%conBeforeUpdate", "color: orange");
  // console.log(`--countRef.value.innerHTML: ${countRef.value.innerHTML}`);
  // console.log(`--count.value: ${count.value}`);
});
onUpdated(() => {
  console.log("%conUpdate", "color: orange");
  // console.log(`--countRef.value.innerHTML: ${countRef.value.innerHTML}`);
  // console.log(`--count.value: ${count.value}`);
});
onBeforeUnmount(() => {
  console.log("%conBeforeUnmount", "color: orange");
  // console.log(`--countRef.value.innerHTML: ${countRef.value.innerHTML}`);
  // console.log(`--count.value: ${count.value}`);
});
onUnmounted(() => {
  console.log("%conUnmounted", "color: orange");
  // console.log(`--countRef.value: ${countRef.value}`);
  // console.log(`--count.value: ${count.value}`);
});
</script>
