# passchain
## Inspiration
We implemented a password manager over the Algorand blockchain. With this, our manager is
not vulnerable anymore to server attacks or influences of the environment.

## What it does
Our password manager uses the Algorand blockchain. For every action in the manager an Algorand transaction will be executed. This transaction will contain encrypted data. By considering these transactions the current situation of a specific PassChain account can be calcualted. The encryption is based on the hash of a masterpassword that the user decides at the beginning of his/her PassChain journey.

## How we built it
Since the primary part of our app are the backend calculations plus sending and reading transactions, the main part of our project is build in python using the Algorand SDK. Apart from this, our frontend is based on ReactJS. To connect frontend and backend we implemented a Flask API in python.

## Challenges we ran into
Properly talking to the blockchain was of course one of hardest and time intensive issues, but also the challenge with the greates learning effect. To set it all up and to use Sandbox and the other environments did bring up issues, which we needed to face to be able to understand Algorand a little bit better. 
The ensurence of a safe usage of our manager is our highest priority. Therefore a considerable amount of time needed to be invested in our encryption method.
Furthermore, challenges during the integration on the other hand also were present. Such issues are good reminders that in projects not everything will work as expected, even if one knows the related subject.


## Accomplishments that we're proud of
The main accomplishment of our project is the understanding of the transactions in the Algorand blockchain. This means, how one can write, read, and interpretate them. Another mayor aspect is the ability to first encrypt the users data, make it unreadable for everyone else and only decrypt it for the correct customer. Next to the backend, to build a friendly and nice-looking frotend and furthermore to connect it with the backend  are also accomplishments that we are very proud of.

## What we learned
I think the main aspects of our learning process are already listed in our accomplishments. However, the main learning was definitivly related to the context of blockchain, more specific Algorand. Different new aspects in programming with JavaScript and Python are always a part of such a work. One more aspect worth to mention is the knowledge gain about the management of group projects.

## What's next for PassChain
Since not all functionalties could be correctly implemented in time, the next steps will be primary to increase the user experience. More specific that the user will be able to update and delete his current entries. To use PassChain as a browser extension to automatically fill login and passwords.
