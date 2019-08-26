<?php
$servername = "localhost";
$username = "csc412";
$password = "csc412";
$dbname = "csc412";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT name, email FROM createatable";
$result = $conn->query($sql);

if ($conn->multi_query($sql) === TRUE) {
    echo "name: " . $_POST["name"]. "   email: " . $_POST["email"]. "<br>";

} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
<body>
    <font size="10" color="red"> Welcome <?php echo $_POST["name"]; ?> !!!</font>
<?php
        // put your code here
        header('Refresh: 4; URL=http://csc412sfsu.com/~jhuang27/index.html');
        
        ?></body>