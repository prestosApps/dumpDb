<!doctype html>
<html>
<head>
        <title>Dib-Dab-Dump!</title>
        <link href="jquery-ui.css" rel="stylesheet"/>
        <script src="external/jquery/jquery.js"></script>
        <script src="jquery-ui.js"></script>
</head>
<body>
<div class="ui-widget-header" style="text-align:center;">
        <h1 class="ui-widget">DumpDb - The biggest dump you'll ever have</h1>
</div>
<div class="ui-content">
<p>
Number of aircraft you have observed is
<?php
    
    $db = new SQLite3('/var/lib/dumpDb/dump1090.db');
    $result = $db->query('select count(distinct(hexcode)) from aircraft;');
    $resultArray = $result->fetchArray();
    echo $resultArray[0]; 
?>
</div>
</body>
</html>

