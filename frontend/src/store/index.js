import { ref } from "vue";

const todoList = ref([]);

export function useTodo() {
  return {
    todoList,
  };
}
