import os
import random
import shutil

splitsize= .85
categories= []

source_folder= "D:/Garbage/garbage_classification"
folders= os.listdir(source_folder)
print(folders)

for subfolder in folders:
    if os.path.isdir(source_folder+'/'+subfolder) :
        categories.append(subfolder)

categories.sort()
print(categories)

target_folder= "D:/Garbage/dataset_for_model"
existDatasetPath= os.path.exists(target_folder)
if existDatasetPath==False:
    os.mkdir(target_folder)

def split_data(SOURCE, TRAINING, VALIDATION, SPLIT_SIZE):
    files= []
    for filename in os.listdir(SOURCE):
        file= SOURCE + filename
        print(file)
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(filename,"is empty !!")
    print(len(files))
    trainingLength= int(len(files) * SPLIT_SIZE)
    shuffleSet= random.sample(files, len(files))
    trainingSet= shuffleSet[0:trainingLength]
    validSet= shuffleSet[trainingLength:]

    for filename in trainingSet:
        thisFile= SOURCE + filename
        dest= TRAINING + filename
        shutil.copyfile(thisFile, dest)

    for filename in validSet:
        thisFile= SOURCE + filename
        dest= VALIDATION + filename
        shutil.copyfile(thisFile, dest)

trainPath= target_folder + "/train"
validatePath= target_folder + "/validate"

existDatasetPath = os.path.exists(trainPath)
if existDatasetPath == False:
    os.mkdir(trainPath)

existDatasetPath = os.path.exists(validatePath)
if existDatasetPath == False:
    os.mkdir(validatePath)

for category in categories:
    trainDesPath= trainPath + '/' + category
    validateDesPath= validatePath + '/' + category

    if os.path.exists(trainDesPath) == False:
        os.mkdir(trainDesPath)

    if os.path.exists(validateDesPath) == False:
        os.mkdir(validateDesPath)

    sourcePath = source_folder + '/' + category + '/'
    trainDesPath = trainDesPath + '/'
    validateDesPath = validateDesPath + '/'

    print("Copy from " + sourcePath + ' to ' + trainDesPath + ' and '+ validateDesPath)
    split_data(sourcePath, trainDesPath, validateDesPath, splitsize)