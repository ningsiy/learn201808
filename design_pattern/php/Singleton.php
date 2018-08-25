<?php

/**
 * 单例模式
 * Class Singleton
 * Ywx
 */

class Singleton
{
    private static $_instance = null;

    /**
     * 防止在外部实例化对象
     * Singleton constructor.
     */
    private function __construct(){
        echo 'Singleton()的实例化对象<br/>';

    }

    /**
     * 实例化
     * @return null|Singleton
     */
    static public function getInstance(){
        if (is_null(self::$_instance)){
            self::$_instance = new Singleton();
        }
        return self::$_instance;
    }

    /**
     * 阻止在外部克隆对象
     */
    private function __clone()
    {
        // TODO: Implement __clone() method.
    }
}

$sin1 = Singleton::getInstance();
$sin2 = Singleton::getInstance();

if ($sin1 === $sin2){
    echo '同一实例化对象';
}else{
    echo '不同的实例化对象';
}