import logo from "../Assets/Images/favicon.webp";
export default function navbar() {
  return (
    <div>
      <nav className="bg-[#00000020] backdrop-blur-3xl backdrop-opacity-25 px-10 py-3 text-2xl w-full shadow-lg flex align-middle">
        <a className="navbar-brand flex flex-row" href="#">
          <img src={logo} className="w-8 mr-3"></img>
          My Polls
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
      </nav>
    </div>
  );
}
