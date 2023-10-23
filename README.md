#бот, конвертируйщий jpg фото в png и обратно 
#человек кидает фото 
  #проверяется его формат jpg или png
     #если его формат оказывается jpg то переводим фото в формат png и выводим фото
     #если его формат оказывается png то переводим фото в формат jpg и выводим фото
     #иначе если фото в ином формате вывести сообщение "фото не соответствует формату
     
     
     
end
JPG в PNG:
import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

shape = builder.insert_image("Input.jpg")
shape.image_data.save("Output.png")
PNG в JPG:
import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

shape = builder.insert_image("Input.png")
shape.image_data.save("Output.jpg")