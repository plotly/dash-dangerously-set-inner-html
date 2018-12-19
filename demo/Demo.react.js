import React, {Component} from 'react';
import { DangerouslySetInnerHTML } from '../src';

class Demo extends Component {
    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return (
            <div>
                <h1>dash-dangerously-set-inner-html Demo</h1>

                <hr/>
                <h2>ExampleComponent</h2>
                <DangerouslySetInnerHTML
                    label="This is an example label"
                    value={this.state.value}
                    setProps={newProps => this.setState({value: newProps.value})}
                />
                <hr/>
            </div>
        );
    }
}

export default Demo;
