<?php
/**
 * 适配器模式
 * Ywx
 */

abstract class MobileUnlock
{
    public abstract function unlock();
}

class PwdUnlock extends MobileUnlock
{
    public function unlock()
    {
        echo '密码解锁<br />';
    }
}

class FingerprintUnlock extends MobileUnlock
{
    public function unlock()
    {
        echo '指纹解锁<br />';
    }
}

/**
 * Class FaceUnlock
 * 待适配
 */
class FaceUnlock
{
    public function face_unclock()
    {
        echo '人脸解锁';
    }
}

class Adapter extends MobileUnlock
{
    private $face;
    public function __construct()
    {
        $this->face = new FaceUnlock();
    }

    public function unlock()
    {
        $this->face->face_unclock();
    }
}

$unlock_type = rand(0, 2);
print($unlock_type.' ');
if ($unlock_type == 0){
    $unlock_type = new PwdUnlock();
}elseif($unlock_type == 1) {
    $unlock_type = new FingerprintUnlock();
}else{
    $unlock_type = new Adapter();
}

$unlock_type->unlock();



