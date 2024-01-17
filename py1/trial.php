<?php 
    session_start():

    echo "<DOCTYPE html>\n<html><head>";

    required_once "functions.php";

    $userstr = ' (Guest)';

    if(isset($_SESSION['user']))