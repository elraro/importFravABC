import MySQLdb as mdb
import querys as querys

DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "frav_ABC"

con = None

con = mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute(querys.query_fir_logitech_fluorescente_data)
cur.execute(querys.query_fir_logitech_halogeno_data)
cur.execute(querys.query_fir_logitech_led_data)
cur.execute(querys.query_fir_logitech_nir_data)
cur.execute(querys.query_fir_microsoft_fluorescente_data)
cur.execute(querys.query_fir_microsoft_halogeno_data)
cur.execute(querys.query_fir_microsoft_led_data)
con.commit()

with open("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_fluorescente_data.txt") as f:
    print("Leyendo logitech_fluorescente_data.txt")
    lines = f.readlines()
    data = lines[1:]  # remove first 1 elements
    for line in data:
        l = line.replace("\n","").split(",")
        var_string = ', '.join(["%s"] * len(l))
        query_string = "INSERT INTO `frav_ABC`.`fir_logitech_fluorescente_data` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
        try:
            cur.execute(query_string, l)
            con.commit()
        except Exception as e:
            print("Error en logitech_fluorescente_data.")
            print(l)
            print(query_string)
            print("Error: " + e)
            con.rollback()

with open("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_halogeno_data.txt") as f:
    print("Leyendo logitech_halogeno_data.txt")
    lines = f.readlines()
    data = lines[1:]  # remove first 1 elements
    for line in data:
        l = line.replace("\n","").split(",")
        var_string = ', '.join(["%s"] * len(l))
        query_string = "INSERT INTO `frav_ABC`.`fir_logitech_halogeno_data` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
        try:
            cur.execute(query_string, l)
            con.commit()
        except Exception as e:
            print("Error en logitech_halogeno_data.")
            print(l)
            print(query_string)
            print("Error: " + e)
            con.rollback()

with open("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_led_data.txt") as f:
    print("Leyendo logitech_led_data.txt")
    lines = f.readlines()
    data = lines[1:]  # remove first 1 elements
    for line in data:
        l = line.replace("\n","").split(",")
        var_string = ', '.join(["%s"] * len(l))
        query_string = "INSERT INTO `frav_ABC`.`fir_logitech_led_data` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
        try:
            cur.execute(query_string, l)
            con.commit()
        except Exception as e:
            print("Error en logitech_led_data.")
            print(l)
            print(query_string)
            print("Error: " + e)
            con.rollback()

with open("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/logitech_nir_data.txt") as f:
    print("Leyendo logitech_nir_data.txt")
    lines = f.readlines()
    data = lines[1:]  # remove first 1 elements
    for line in data:
        l = line.replace("\n","").split(",")
        var_string = ', '.join(["%s"] * len(l))
        query_string = "INSERT INTO `frav_ABC`.`fir_logitech_nir_data` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
        try:
            cur.execute(query_string, l)
            con.commit()
        except Exception as e:
            print("Error en logitech_nir_data.")
            print(l)
            print(query_string)
            print("Error: " + e)
            con.rollback()

with open("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/microsoft_fluorescente_data.txt") as f:
    print("Leyendo microsoft_fluorescente_data.txt")
    lines = f.readlines()
    data = lines[1:]  # remove first 1 elements
    for line in data:
        l = line.replace("\n","").split(",")
        var_string = ', '.join(["%s"] * len(l))
        query_string = "INSERT INTO `frav_ABC`.`fir_microsoft_fluorescente_data` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
        try:
            cur.execute(query_string, l)
            con.commit()
        except Exception as e:
            print("Error en microsoft_fluorescente_data.")
            print(l)
            print(query_string)
            print("Error: " + e)
            con.rollback()

with open("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/microsoft_halogeno_data.txt") as f:
    print("Leyendo microsoft_halogeno_data.txt")
    lines = f.readlines()
    data = lines[1:]  # remove first 1 elements
    for line in data:
        l = line.replace("\n","").split(",")
        var_string = ', '.join(["%s"] * len(l))
        query_string = "INSERT INTO `frav_ABC`.`fir_microsoft_halogeno_data` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
        try:
            cur.execute(query_string, l)
            con.commit()
        except Exception as e:
            print("Error en microsoft_halogeno_data.")
            print(l)
            print(query_string)
            print("Error: " + e)
            con.rollback()

with open("/media/alberto/Datos/FRAV_ALBERTO/FIR/DATA/microsoft_led_data.txt") as f:
    print("Leyendo microsoft_led_data.txt")
    lines = f.readlines()
    data = lines[1:]  # remove first 1 elements
    for line in data:
        l = line.replace("\n","").split(",")
        var_string = ', '.join(["%s"] * len(l))
        query_string = "INSERT INTO `frav_ABC`.`fir_microsoft_led_data` (clase,file,locateFace,faceConfidence,locateEyes,eye0Confidence,eye1Confidence,age,backgroundUniformity,chin,crown,deviationFromFrontalPose,deviationFromUniformLighting,ear0,ear1,ethnicityAsian,ethnicityBlack,ethnicityWhite,exposure,eye0X,eye0Y,eye0GazeFrontal,eye0Open,eye0Red,eye0Tinted,eye1X,eye1Y,eye1GazeFrontal,eye1Open,eye1Red,eye1Tinted,eyeDistance,faceCenterX,faceCenterY,glasses,grayScaleDensity,height,hotSpots,isColor,isMale,lengthOfHead,mouthClosed,naturalSkinColour,numberOfFaces,poseAngleRoll,sharpness,width,widthOfHead,ISO_19794_5_EyesGazeFrontalBestPractice,ISO_19794_5_EyesNotRedBestPractice,ISO_19794_5_EyesOpenBestPractice,ISO_19794_5_GoodExposure,ISO_19794_5_GoodGrayScaleProfile,ISO_19794_5_GoodVerticalFacePosition,ISO_19794_5_HasNaturalSkinColour,ISO_19794_5_HorizontallyCenteredFace,ISO_19794_5_ImageWidthToHeightBestPractice,ISO_19794_5_IsBackgroundUniformBestPractice,ISO_19794_5_IsBestPractice,ISO_19794_5_IsCompliant,ISO_19794_5_IsFrontal,ISO_19794_5_IsFrontalBestPractice,ISO_19794_5_IsLightingUniform,ISO_19794_5_IsSharp,ISO_19794_5_LengthOfHead,ISO_19794_5_LengthOfHeadBestPractice,ISO_19794_5_MouthClosedBestPractice,ISO_19794_5_NoHotSpots,ISO_19794_5_NoTintedGlasses,ISO_19794_5_OnlyOneFaceVisible,ISO_19794_5_Resolution,ISO_19794_5_ResolutionBestPractice,ISO_19794_5_WidthOfHead,ISO_19794_5_WidthOfHeadBestPractice,Features_Ethnicity,Features_Gender,Features_WearsGlasses) VALUES (%s);" % var_string
        try:
            cur.execute(query_string, l)
            con.commit()
        except Exception as e:
            print("Error en microsoft_led_data.")
            print(l)
            print(query_string)
            print("Error: " + e)
            con.rollback()

con.close()
