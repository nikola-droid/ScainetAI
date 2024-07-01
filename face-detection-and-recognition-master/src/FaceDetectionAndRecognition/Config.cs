namespace FaceDetectionAndRecognition
{
    public static class Config
    {
        public static string FacePhotosPath = "Source\\Faces\\";
        public static string FaceListTextFile = "Source\\FaceList.txt";
        public static string HaarCascadePath = "Resources\\haarcascade_frontalface_default.xml";
        public static int TimerResponseValue = 150;
        public static string ImageFileExtension = "eng.png";
        public static int ActiveCameraIndex = 0;//0: Default active camera device
    }
}
