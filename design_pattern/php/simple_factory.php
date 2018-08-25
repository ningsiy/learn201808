<?php
/**
 * 简单工厂
 * User: Ywx
 */


/**
 * 定义电脑接口
 * Interface Computer
 */
interface Computer
{
    public function createComputer();
}

/**
 * Class Dell
 * 实现电脑接口 （戴尔电脑制造商）
 */
class Dell implements Computer
{
    public function createComputer()
    {
        echo '戴尔笔记本<br/>';
    }
}

/**
 * Class Asus
 * 实现电脑接口 （华硕电脑制造商）
 */
class Asus implements Computer
{
    public function createComputer()
    {
        echo '华硕笔记本<br/>';
    }
}

/**
 * Class SimpleFactory
 * 简单工厂类
 */
class SimpleFactory
{
    public static function buy_dell(){
        return new Dell();
    }

    public static function buy_asus(){
        return new Asus();
    }
}

$dell = SimpleFactory::buy_dell();
$asus = SimpleFactory::buy_asus();
$dell->createComputer();
$asus->createComputer();