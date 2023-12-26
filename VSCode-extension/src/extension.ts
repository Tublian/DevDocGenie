import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
	console.log('Congratulations, your extension "devdocgenie" is now active!');

	let disposable = vscode.commands.registerCommand('devdocgenie.helloWorld', () => {
		vscode.window.showInformationMessage('Hello World from DevDocGenie!');
	});

	context.subscriptions.push(vscode.commands.registerCommand('chatContainer.openChat', () => {
		const panel = vscode.window.createWebviewPanel(
			'chatView',
			'Chat',
			vscode.ViewColumn.One,
			{}
		);

		panel.webview.html = getWebviewContent();
	}));

	context.subscriptions.push(disposable);
}


export function deactivate() { }


function getWebviewContent() {
	return `
        <html>
        <body>
            <h1>Chat</h1>
			<p>demo</p>
        </body>
        </html>`;
}