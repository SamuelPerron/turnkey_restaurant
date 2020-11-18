import axios from 'axios';
import AOS from 'aos';

import './global-styles.scss';
import 'aos/dist/aos.css';

import ObjectList from '../components/ObjectList';


function App() {
    return (
        <div className="App">
            <ObjectList />
        </div>
    );
}

export default App;
