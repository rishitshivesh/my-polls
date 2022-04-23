import axios from "axios";

console.log(localStorage.getItem("polls_access_token"));
// localStorage.removeItem("polls_access_token");
const instance = axios.create({
  baseURL: "localhost:8000/api",
  headers: {
    Authorization: localStorage.getItem("polls_access_token"),
  },
});

export default instance;
