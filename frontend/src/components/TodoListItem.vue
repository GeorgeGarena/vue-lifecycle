<template>
  <div :class="{ completed }" ref="itemRef">{{ title }}</div>
</template>
<script setup>
import { ref, onMounted, onUpdated } from "vue";
const props = defineProps({
  title: String,
  completed: Boolean,
});
const itemRef = ref(null);

onMounted(() => {
  // console.log("onMounted: todo list item");
});
onUpdated(() => {
  // console.log("onUpdated", props.completed);
  // itemRef.value.scrollIntoView();
});
</script>
<style>
.completed {
  text-decoration: line-through;
}
</style>
