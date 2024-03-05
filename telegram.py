import telebot
import sqlite3
from telebot import types
# from constants import API_KEY
from datetime import datetime
API_KEY =  "128795640:AAEZl-jhKYgwzxQdVHFv"

bot = telebot.TeleBot(API_KEY, parse_mode=None)

# bot

#start

@bot.message_handler(commands=["start"])
def send_help_message(msg: types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton("/help")
    button2 = types.KeyboardButton("/Workout")
    button3 = types.KeyboardButton("/Food")
    keyboard.add(button1, button2, button3)
    bot.send_message(msg.chat.id, "Please choose an option:", reply_markup=keyboard)









@bot.message_handler(func=lambda message: message.text in ["/help"])
def handle_command(message):
    if message.text == "/help":
        bot.send_message(message.chat.id, "GANRAP Gym is a bot that helps you knowing the exercises for each muscle with angles, & also some training schedules with different systems for a month.\n\nFor example:\nPush/Pull Leg - two muscles a day\nUpper/Lower - 1 muscle a day\n\nWe will also be adding diets in future, in addition for a calories calculator to measure your requirements either for cutting or bulking or maintaining your healthy proper weight!\n\nAlso there will be a calculation for your protein requirements depending on your height, weight, & diets that you selected previously!\n\nWe will be also adding the most popular meals that are rich with carbohydrates, Fats, & fibers\n\nGANRAP GYM! KEEP UP WITH THE MEN!!")
    


# Food
@bot.message_handler(func=lambda message: message.text == "/Food")
def handle_food_health_command(message):
    food_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    bulking_button = types.KeyboardButton("Bulking")
    cutting_button = types.KeyboardButton("Cutting")
    item0 = "Back to Main Menu"
    food_keyboard.add(bulking_button, cutting_button)
    food_keyboard.row(item0) 
    bot.send_message(message.chat.id, "Please choose an option:", reply_markup=food_keyboard)

    @bot.message_handler(func=lambda message: message.text == "Back to Main Menu")
    def handle_back_to_main_menu_command(message):
        send_help_message(message)

@bot.message_handler(func=lambda message: message.text in ["Bulking", "Cutting"])
def handle_food_option(message):
    if message.text == "Bulking":
        bot.send_message(message.chat.id, "Coming soon!!!")
    elif message.text == "Cutting":
        bot.send_message(message.chat.id, "Coming soon!!")


# Workout
@bot.message_handler(func=lambda message: message.text == "/Workout")
def handle_workout_command(message):
    workout_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    chest_button = types.KeyboardButton("Chest")
    shoulders_button = types.KeyboardButton("Shoulders")
    back_button = types.KeyboardButton("Back")
    triceps_button = types.KeyboardButton("Triceps")
    biceps_button = types.KeyboardButton("Biceps")
    leg_button = types.KeyboardButton("Leg")
    cardio_button = types.KeyboardButton("Cardio")
    item1 = "Back to Main Menu"
    workout_keyboard.add(chest_button, shoulders_button, back_button, triceps_button, biceps_button, leg_button, cardio_button)
    workout_keyboard.row(item1)
    bot.send_message(message.chat.id, "Please choose a muscle:", reply_markup=workout_keyboard)

    @bot.message_handler(func=lambda message: message.text == "Back to Main Menu")
    def handle_back_to_main_menu_command(message):
        send_help_message(message)


#CHEST

@bot.message_handler(func=lambda message: message.text == "Chest")
def handle_chest_command(message):
    chest_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    upper_chest_button = types.KeyboardButton("Upper chest")
    lower_chest_button = types.KeyboardButton("Lower chest")
    middle_chest_button = types.KeyboardButton("Middle chest")
    item2 = "Back to workout Menu"
    chest_keyboard.add(upper_chest_button, lower_chest_button, middle_chest_button)
    chest_keyboard.row(item2)
    bot.send_message(message.chat.id, "Please choose a chest area:", reply_markup=chest_keyboard)
    

    @bot.message_handler(func=lambda message: message.text == "Back to workout Menu")
    def handle_back_to_workout_menu_command(message):
        handle_workout_command(message)





#SHOULDERS

@bot.message_handler(func=lambda message: message.text == "Shoulders")
def handle_shoulders_command(message):
    shoulders_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    anterior_head_button = types.KeyboardButton("Anterior Head")
    lateral_head_button = types.KeyboardButton("Lateral Head")
    posterior_head_button = types.KeyboardButton("Posterior Head")
    item3 = "Back to workout Menu"
    shoulders_keyboard.add(anterior_head_button, lateral_head_button, posterior_head_button)
    shoulders_keyboard.row(item3)
    bot.send_message(message.chat.id, "Please choose a Shoulders area:", reply_markup=shoulders_keyboard)

    @bot.message_handler(func=lambda message: message.text == "Back to workout Menu")
    def handle_back_to_workout_menu_command(message):
        handle_workout_command(message)

@bot.message_handler(func=lambda message: message.text in ["Anterior Head", "Lateral Head", "Posterior Head"])
def handle_shoulders_area_command(message):
    bot.send_message(message.chat.id, "You have chosen the " + message.text + " workout.")


#BACK


@bot.message_handler(func=lambda message: message.text == "Back")
def handle_back_command(message):
    back_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    rotator_cuff_button = types.KeyboardButton("Rotator Cuff")
    lats_back_button = types.KeyboardButton("Lats")
    upper_traps_back_button = types.KeyboardButton("Upper Traps")
    lower_Traps_back_button = types.KeyboardButton("Lower Traps")
    spinae_erector_back_button = types.KeyboardButton("Spinae Erector")
    teres_major_back_button = types.KeyboardButton("Teres Major")
    item4 = "Back to workout Menu"
    back_keyboard.add(rotator_cuff_button, lats_back_button, upper_traps_back_button, lower_Traps_back_button, spinae_erector_back_button, teres_major_back_button)
    back_keyboard.row(item4)
    bot.send_message(message.chat.id, "Please choose a Back area:", reply_markup=back_keyboard)

    @bot.message_handler(func=lambda message: message.text == "Back to workout Menu")
    def handle_back_to_workout_menu_command(message):
        handle_workout_command(message)

@bot.message_handler(func=lambda message: message.text in ["Rotator Cuff", "Lats", "Upper Traps", "Lower Traps", "Spinae Erector", "Teres Major"])
def handle_back_area_command(message):
    bot.send_message(message.chat.id, "You have chosen the " + message.text + " workout.")


#Triceps


@bot.message_handler(func=lambda message: message.text == "Triceps")
def handle_triceps_command(message):
    triceps_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    lateral_head_button = types.KeyboardButton("Lateral Head")
    long_head_button = types.KeyboardButton("Long Head")
    medial_head_button = types.KeyboardButton("Medial Head (Hidden)")
    item5 = "Back to workout Menu"
    triceps_keyboard.add(lateral_head_button, long_head_button, medial_head_button)
    triceps_keyboard.row(item5)
    bot.send_message(message.chat.id, "Please choose a Triceps area:", reply_markup=triceps_keyboard)

    @bot.message_handler(func=lambda message: message.text == "Back to workout Menu")
    def handle_back_to_workout_menu_command(message):
        handle_workout_command(message)

@bot.message_handler(func=lambda message: message.text in ["Lateral Head", "Long Head", "Medial Head (Hidden)"])
def handle_triceps_area_command(message):
    bot.send_message(message.chat.id, "You have chosen the " + message.text + " workout.")



#BICEPS


@bot.message_handler(func=lambda message: message.text == "Biceps")
def handle_biceps_command(message):
    biceps_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    long_head_button = types.KeyboardButton("Long Head")
    short_head_button = types.KeyboardButton("Short Head")
    brachialis_button = types.KeyboardButton("Brachialis")
    item6 = "Back to workout Menu"
    biceps_keyboard.add(long_head_button, short_head_button, brachialis_button)
    biceps_keyboard.row(item6)
    bot.send_message(message.chat.id, "Please choose a Biceps area:", reply_markup=biceps_keyboard)

    @bot.message_handler(func=lambda message: message.text == "Back to workout Menu")
    def handle_back_to_workout_menu_command(message):
        handle_workout_command(message)

@bot.message_handler(func=lambda message: message.text in ["Long Head", "Short Head", "Brachialis"])
def handle_biceps_area_command(message):
    bot.send_message(message.chat.id, "You have chosen the " + message.text + " workout.")



#LEGS
 

@bot.message_handler(func=lambda message: message.text == "Leg")
def handle_leg_command(message):
    leg_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    front_quads_button = types.KeyboardButton("Front Quads")
    medialis_quads_button = types.KeyboardButton("Medialis Quads")
    lateralis_quads_button = types.KeyboardButton("Lateralis Quads")
    glutes_button = types.KeyboardButton("Glutes")
    hamstring_button = types.KeyboardButton("Hamstring")
    calves_button = types.KeyboardButton("Calves")
    item7 = "Back to workout Menu"
    leg_keyboard.add(front_quads_button, medialis_quads_button, lateralis_quads_button, glutes_button, hamstring_button, calves_button)
    leg_keyboard.row(item7)
    bot.send_message(message.chat.id, "Please choose a leg area:", reply_markup=leg_keyboard)

    @bot.message_handler(func=lambda message: message.text == "Back to workout Menu")
    def handle_back_to_workout_menu_command(message):
        handle_workout_command(message)


@bot.message_handler(func=lambda message: message.text in ["Front Quads", "Medialis Quads", "Lateralis Quads", "Glutes", "Hamstring", "Calves"])
def handle_leg_area_command(message):
    bot.send_message(message.chat.id, "You have chosen the " + message.text + " workout.")



bot.polling()






#     bot.send_photo(message.chat.id, media)
# @bot.message_handler(func=lambda message: message.text in ["Upper chest", "Lower chest", "Middle chest"])
# def handle_chest_area_command(message):
#     bot.send_message(message.chat.id, "You have chosen the " + message.text + " workout.")


# # Define global variable to store media URLs
# media = []

# # Function to handle the "Upper Chest" area command
# @bot.message_handler(func=lambda message: message.text == "Upper Chest")
# def handle_upper_chest_area_command(message):
#     # Clear the media list
#     media.clear()

#     # Add the media URLs to the list
#     media.append("https://t.me/GanrapGym/2")
#     media.append("https://t.me/GanrapGym/3")
#     media.append("https://t.me/GanrapGym/4")
    
#     # "if message.photo and message.photo[-1].file_id in media:
#     #   index = media.index(message.photo[-1].file_id) + 1"


#     # Send the first photo to the user
#     bot.send_photo(message.chat.id, media[0])
    
#     # Ask the user if they want to see the next photo
#     next_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     next_button = types.KeyboardButton("Next")
#     next_keyboard.add(next_button)
#     bot.send_message(message.chat.id, "Do you want to see the next photo?", reply_markup=next_keyboard)

# # Function to handle the "Next" button press
# @bot.message_handler(func=lambda message: message.text == "Next")
# def handle_next_command(message):
#     # Get the index of the next photo
#     index = media.index(message.photo[-1].file_id) + 1
    
#     # If there are more photos, send the next one
#     if index < len(media):
#         bot.send_photo(message.chat.id, media[index])
        
#         # Ask the user if they want to see the next photo
#         next_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#         next_button = types.KeyboardButton("Next")
#         next_keyboard.add(next_button)
#         bot.send_message(message.chat.id, "Do you want to see the next photo?", reply_markup=next_keyboard)
#     else:
#         # If there are no more photos, send a message to the user
#         bot.send_message(message.chat.id, "There are no more photos.")


