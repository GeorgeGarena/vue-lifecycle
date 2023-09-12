<template>
  <div class="todo-list">
    <h2>Todo list</h2>
    <div>
      <input id="input" ref="inputRef" type="text" v-model="inputText" />
      <button @click="inputText && createTodo()">create todo</button>
    </div>
    <span ref="textRef" :style="{ width: 'auto' }">{{ inputText }}</span>
    <div ref="">
      <ul>
        <li v-for="(todo, idx) of todoList" :key="idx">
          <TodoListItem :title="todo.title" :completed="todo.completed" />
          <div class="actions">
            <button
              class="update"
              @click="updateTodo(todo.id, !todo.completed)"
            >
              Update
            </button>
            <button class="delete" @click="deleteTodo(todo.id)">Delete</button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
<script setup>
import { ref, onUpdated } from "vue";
import TodoListItem from "./TodoListItem.vue";

const inputText = ref("");
const inputRef = ref(null);
const textRef = ref(null);
const todoList = ref([]);

async function getTodos() {
  const data = await fetch("/api/get_todos").then((res) => res.json());
  todoList.value = data.todos;
}
async function createTodo() {
  const newTodo = await fetch("/api/create_todo", {
    method: "POST",
    body: JSON.stringify({
      title: inputText.value,
    }),
  }).then((res) => res.json());

  inputText.value = "";
  todoList.value.push(newTodo);
}
async function updateTodo(id, completed) {
  const updatedTodo = await fetch("/api/update_todo", {
    method: "POST",
    body: JSON.stringify({ id, completed }),
  }).then((res) => res.json());

  const todo = todoList.value.find((item) => item.id === id);
  todo.completed = updatedTodo.completed;
}
async function deleteTodo(id) {
  const deletedTodo = await fetch("/api/delete_todo", {
    method: "POST",
    body: JSON.stringify({ id }),
  }).then((res) => res.json());
  todoList.value = todoList.value.filter((item) => item.id !== deletedTodo.id);
}
getTodos();

function getRandomColor() {
  return "#" + ((Math.random() * 0xffffff) << 0).toString(16);
}

onUpdated(() => {
  if (textRef.value.getBoundingClientRect().width > 100) {
    inputRef.value.style.backgroundColor = getRandomColor();
  } else {
    inputRef.value.style.backgroundColor = "#000";
  }
});
</script>
<style>
ul {
  display: flex;
  flex-direction: column;
  padding: 0;
}
li {
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #fff;
  border-radius: 5px;
  padding: 5px;
  margin: 5px;
  width: 100%;
}
.actions {
  display: flex;
}
.update {
  display: block;
  border: 1px solid orange;
  color: orange;
}
.delete {
  display: block;
  border: 1px solid red;
  color: red;
  font-weight: bolder;
}
</style>
