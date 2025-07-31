# trivy-UI

## Overview

**trivy-UI** is a user interface project designed to simplify the use of [Trivy](https://github.com/aquasecurity/trivy), a popular open-source vulnerability and misconfiguration scanner for containers, filesystems, and Git repositories. This UI aims to make it easier to run scans, view reports, and manage results visually.

## Features
- Run Trivy scans from the UI
- Upload and analyze scan reports
- Visualize vulnerabilities and misconfigurations
- Filter and sort scan results
- Export reports in various formats                 

## Getting Started

### Prerequisites
- [Node.js](https://nodejs.org/) (for UI development)
- [Trivy](https://github.com/aquasecurity/trivy) installed and available in your system PATH

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/Ampenzi/trivy-UI.git
   cd trivy-UI
   ```
2. Install dependencies:
   ```sh
   npm install
   ```

### Running the App
Start the development server:
```sh
npm start
```
The UI will be available at `http://localhost:3000` (or as specified in the output).

### Using Trivy with the UI
- Ensure Trivy is installed and accessible from the command line.
- Use the UI to trigger scans or upload existing Trivy JSON reports for visualization.

## Project Structure
- `src/` - Main source code for the UI
- `public/` - Static assets
- `README.md` - Project documentation

## Contributing
Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.