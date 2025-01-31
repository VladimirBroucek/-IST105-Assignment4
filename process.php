<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $a = $_POST['a'];
    $b = $_POST['b'];
    $c = $_POST['c'];

    if (!is_numeric($a) || !is_numeric($b) || !is_numeric($c)) {
        die("Error: All values must be numeric.");
    }

    $command = escapeshellcmd("python3 calculate.py $a $b $c");
    $output = shell_exec($command);

    echo "<h2>Calculation Result</h2>.";
    echo "<div>$output</div>";
} else {
    echo "<div>Invalid request</div>";
}

?>
