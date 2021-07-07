import array


resolutions = array.array('i',[
    414,600,768,800,960,1024,1280,1366,1440,1536,1600,1920
]) #Популярные ширины области просмотра для адаптивной вёрстки на данный момент

result = ""
start_template = "@media only all and ("
end_template = "px){}\n"

for template in resolutions:
    #Выбираются максимальные значения областей просмотра в адаптивном дизайне
    result += start_template+"max-width: "+str(template)+end_template
    
result += start_template+"min-width: "+str(resolutions[-1])+end_template

print(result)
