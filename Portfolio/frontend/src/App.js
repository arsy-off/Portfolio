import React, { Component } from "react"

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: {
        title: "",
        logo: ""
      },
      companiesList: []
      };
  }

    async componentDidMount() {
      try {
        const res = await fetch('http://localhost:8000/api/companies/');
        const companiesList = await res.json();
        this.setState({
          companiesList
        });
      } catch (e) {
        console.log(e);
    }
    }
    renderItems = () => {
      return this.state.companiesList.map(item => (
        <li 
          key={item.id}
          className="list-group-item d-flex justify-content-between align-items-center"
        >
          <span>
            {item.title}
          </span>
          <img src={item.logo}></img>
        </li>
      ));
    };

    render() {
      return (
        <main className="content">
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
      </main>
      )
    }
  }
  
export default App;