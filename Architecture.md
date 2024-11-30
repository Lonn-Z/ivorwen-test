#### AssignmentListModel
* Responsibility:  
  * Stores assignment records  
  * Client can query them (indirectly)  
  * Updates records using Webwork and Canvas APIs when client refreshes display  
* Resides on:  
  * Server  
* Communicates with:  
  * UserAssignmentList to send list of assignments  
  * CanvasAPI and WebworkAPI to retrieve tasks

Signature used by UserAssignmentList:  
```java
public List<List<String>> AssignmentList (List<Map<String userId, List<String> AssignmentFields>>) {
	//insert methods
	return all information for all tasks for a particular userId;
}
```


Signature for CanvasAPI and WebworkAPI:  
```java
public List<List<String>> AssignmentList (API with specific userId) {
	//insert methods
	return all updated information for all tasks for a particular userId;
}
```


#### UserAssignmentView
* Responsibility:  
  * Displays all assignments in AssignmentList with userId=(the users specific id) in the user's terminal  
  * Allows users to mark assignments (complete, incomplete, pinned, etc.)  
* Resides on:  
  * Webpage  
* Communicates with:  
  * AssignmentList to fetch and send assignment data.

```java
public void UserAssignmentView(List<String> assignments) {
	// TODO complete this method
}
```


#### CanvasAPI
* Responsibility  
  * Connects the user's Canvas page to AssignmentList. Handles all the refresh and assignment info fetching functions.  
  * Connects UserAssignmentview to the user's canvas page. Handles assignment tagging and completion.  
* Resides on:  
  * Local machine  
* Communicates with:  
  * AssignmentList to send Canvas tasks


#### WebworkAPI
* Responsibility:  
  * Connects to the user’s Webwork account  
  * Retrieves tasks and stores associated information (name, due date, etc.)  
* Resides on:  
  * Local machine  
* Communicates with:  
  * AssignmentList to send Webwork tasks

```java
	public List<String> WebWorkAPI () {
		// insert algorithm here
		List<String> tasks;
		return tasks;
}
```


#### UserAuthenticator
* Responsibility  
  * Receives user credentials and validates whether the password matches the username  
  * Informs the server not to serve any requests made by the client if their credentials were invalid  
* Resides on:  
  * Server  
* Communicates with:  
  * UserCredentialInput  
  * AssignmentList

``` java
	public boolean UserAuthenticator (List<String>) {
		// insert algorithm here
		return true
}
```

#### UserCredentialInputController
* Responsibility  
  * Receive user credentials from the user and send them to the server  
* Resides on:  
  * Client  
* Communicates with:  
  * UserAuthenticator

``` java
	public List<String> UserCredentialInput() {
		// insert algorithm here
		return List.of(username, password);
}
```
