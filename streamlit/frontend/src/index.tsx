import { StreamlitComponentBase, withStreamlitConnection } from "streamlit-component-lib"
import React, { ReactNode } from "react"
import ReactDOM from "react-dom"
import MyComponent from "./MyComponent"

class StreamlitComponent extends StreamlitComponentBase {
  public render = (): ReactNode => {
    return (
      <div>
        <MyComponent />
      </div>
    )
  }
}

const component = withStreamlitConnection(StreamlitComponent)

ReactDOM.render(
  <React.StrictMode>
    {React.createElement(component)}
  </React.StrictMode>,
  document.getElementById("root")
)