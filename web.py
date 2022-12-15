import streamlit as st
import functions_for_todo_list


def add_todo():
    todo = st.session_state["newtodo"] + '\n'
    todos.append(todo)
    functions_for_todo_list.write_todos(todos)


todos = functions_for_todo_list.get_todos()
st.title("My todo app")
st.subheader("This is my todo app")
st.write("This app is a tool to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions_for_todo_list.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new todo",
              on_change=add_todo, key="newtodo")

# st.session_state
# print("the end")