<?php
/**
 * 抽象工厂
 * Ywx
 */

/**
 * Interface MobilePhone
 * 抽象产品
 */
interface MobilePhone
{
    public function call_number();
    public function photo();
}

/**
 * Class XiaoMiMobile
 * 具体产品 （小米手机）
 */
class XiaoMiMobile implements MobilePhone
{
    public function call_number()
    {
        echo '小米手机8,正在通话中...<br />';
    }

    public function photo()
    {
        echo '这是用小米8拍摄的照片！<br />';
    }
}

/**
 * Class MeizuMobile
 * 具体产品 （魅族手机）
 */
class MeizuMobile implements MobilePhone
{
    public function call_number()
    {
        echo '魅族16,正在通话中...<br />';
    }

    public function photo()
    {
        echo '这是用魅族16拍摄的照片！<br />';
    }
}

/**
 * Interface AbstractFactory
 * 抽象工厂
 */
interface Factory
{
    public function create_phone();
}

/**
 * Class XiaoMiFactory
 * 具体工厂 （小米）
 */
class XiaoMiFactory implements Factory
{
    public function create_phone()
    {
        return new XiaoMiMobile();
    }
}

class MeizuFactory implements Factory
{
    public function create_phone()
    {
        return new MeizuMobile();
    }
}

$xiaomi = new XiaoMiFactory();
$meizu = new MeizuFactory();
$xiaomi_phone = $xiaomi->create_phone();
$meizu_phone = $meizu->create_phone();
$xiaomi_phone->call_number();
$xiaomi_phone->photo();
$meizu_phone->call_number();
$meizu_phone->photo();
