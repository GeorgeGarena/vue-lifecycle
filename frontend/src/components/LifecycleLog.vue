<template>
  <div>
    <h2>Lifecycle logs</h2>
    <button @click="count += 1" ref="countRef">count: {{ count }}</button>
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
const count = ref(0);
const countRef = ref(null);

onBeforeMount(() => {
  console.log("%conBeforeMount", "color: green");
  console.log(
    `countRef.value: ${countRef.value}\n`,
    `count.value: ${count.value}`
  );
  // alert("onBeforeMount");
});
onMounted(() => {
  console.log("%conMounted", "color: green");
  console.log(
    `countRef.value: ${countRef.value.innerHTML}\n`,
    `count.value: ${count.value}`
  );
  // alert("onMounted");
});
onBeforeUpdate(() => {
  console.log("%conBeforeUpdate", "color: green");
  console.log(
    `countRef.value.innerHTML: ${countRef.value.innerHTML}\n`,
    `count.value: ${count.value}`
  );
  // alert("onBeforeUpdate");
});
onUpdated(() => {
  console.log("%conUpdate", "color: green");
  console.log(
    `countRef.value.innerHTML: ${countRef.value.innerHTML}\n`,
    `count.value: ${count.value}`
  );
  // alert("onUpdated");
});
onBeforeUnmount(() => {
  console.log("%conBeforeUnmount", "color: green");
  console.log(
    `countRef.value.innerHTML: ${countRef.value.innerHTML}\n`,
    `count.value: ${count.value}`
  );
});
onUnmounted(() => {
  console.log("%conUnmounted", "color: green");
  console.log(
    `countRef.value: ${countRef.value}\n`,
    `count.value: ${count.value}`
  );
});
</script>
