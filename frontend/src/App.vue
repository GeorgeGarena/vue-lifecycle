<template>
  <div>
    <h1>Vue Lifecycle</h1>
    <div>
      <button @click="isLifecycleLog = false">Todo List</button>
      <button @click="isLifecycleLog = true">Lifecycle Log</button>
    </div>
    <LifecycleLog v-if="isLifecycleLog"></LifecycleLog>
    <TodoList v-else></TodoList>
  </div>
</template>
<script setup>
import { ref } from "vue";
import TodoList from "./components/TodoList.vue";
import LifecycleLog from "./components/LifecycleLog.vue";

const isLifecycleLog = ref(false);
</script>
