import React from "react";
import Navbar from "./navbar";
// import API from "../Services/axios";

export default function Home() {
  const token = localStorage.getItem("polls_access_token");
  return (
    <div className="bg-white ">
      <Navbar />
      <div>Hello World!</div>
      {token}
    </div>
  );
}
