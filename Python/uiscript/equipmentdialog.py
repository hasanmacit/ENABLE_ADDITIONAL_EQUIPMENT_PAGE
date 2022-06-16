import app
import player
import item

EQUIPMENT_START_INDEX = player.EQUIPMENT_SLOT_START

import uiScriptLocale
BOARD_WIDTH		= 180
BOARD_HEIGHT	= 290

window = {
	"name" : "EquipmentDialog",
	"style" : ("movable", "float",),
	
	"x" : SCREEN_WIDTH - 180,
	"y" : 95,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : "Ekipman Penceresi",

			"children" :
			(
				## base_tab
				{
					"name" : "base_tab",
					"type" : "image",

					"x" : 12,
					"y" : 33,

					"width" : BOARD_WIDTH,
					"height" : 25,

					"image" : "d:/ymir work/ui/equipment_bg_without_ring_tab00.tga",
				},
				## Tab Area
				{
					"name" : "additional_tab",
					"type" : "window",

					"x" : 12,
					"y" : 33,

					"width" : BOARD_WIDTH,
					"height" : 26,

					"children" :
					[
						{
							"name" : "tab_img_01",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : BOARD_WIDTH,
							"height" : 25,

							"image" : "d:/ymir work/ui/equipment_bg_without_ring_tab01.tga",
						},
						{
							"name" : "tab_img_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : BOARD_WIDTH,
							"height" : 25,

							"image" : "d:/ymir work/ui/equipment_bg_without_ring_tab02.tga",
						},
						{
							"name" : "tab_btn_01",
							"type" : "button",

							"x" : 0,
							"y" : 0,

							"width" : 39,
							"height" : 25,
							"tooltip_text" : "Slot 1",
						},
						{
							"name" : "tab_btn_02",
							"type" : "button",

							"x" : 39,
							"y" : 0,

							"width" : 39,
							"height" : 25,
							"tooltip_text" : "Slot 2",
						},
					],
				},
				## equip area
				{
					"name" : "equipment_window",
					"type" : "window",

					"x" : 0,
					"y" : 56,

					"width" : BOARD_WIDTH,
					"height" : BOARD_HEIGHT,

					"children" :
					[							
						## equipment slots
						{
							"name":"equipment_base_image",
							"type":"image",
							"style" : ("attach",),

							"x" : 0,
							"y" : 0,
							"horizontal_align" : "center",
							"image" : "d:/ymir work/ui/equipment_bg_without_ring.tga",

							"children" :
							(
								{
									"name" : "equipment_slot",
									"type" : "slot",

									"x" : 3,
									"y" : 3,

									"width" : 150,
									"height" : 140,

									"slot" : (
											{"index":EQUIPMENT_START_INDEX+0, "x":39, "y":37, "width":32, "height":64},
											{"index":EQUIPMENT_START_INDEX+1, "x":39, "y":2, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+2, "x":2, "y":98, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+3, "x":75, "y":67, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96},
											{"index":EQUIPMENT_START_INDEX+5, "x":114, "y":67, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+6, "x":114, "y":35, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32},
											{"index":EQUIPMENT_START_INDEX+10, "x":75, "y":35, "width":32, "height":32},
											##{"index":item.EQUIPMENT_RING1, "x":2, "y":106, "width":32, "height":32},
											##{"index":item.EQUIPMENT_RING2, "x":75, "y":106, "width":32, "height":32},
											{"index":item.EQUIPMENT_BELT, "x":39, "y":100, "width":32, "height":32},
									),
								},
								{
									"name" : "unique_slot",
									"type" : "slot",

									"x" : 3,
									"y" : 140,

									"width" : 150,
									"height" : 36,

									"slot" : 
									(
										{"index":EQUIPMENT_START_INDEX+7, "x":4, "y":10, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+8, "x":38, "y":8, "width":32, "height":32},
										## ITEM_UNIQUE_LEFT
										{"index":item.EQUIPMENT_RING1, "x":2, "y":7, "width":32, "height":32},
										## ITEM_UNIQUE_RIGHT
										{"index":item.EQUIPMENT_RING2, "x":39, "y":7, "width":32, "height":32},
									),
								},
							),
						},
						## dragon_soul_button
						{
							"name" : "dragon_soul_button",
							"type" : "button",

							"x" : 18,
							"y" : 186,

							"tooltip_text" : uiScriptLocale.TASKBAR_DRAGON_SOUL,

							"default_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_01.tga",
							"over_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_02.tga",
							"down_image" : "d:/ymir work/ui/dragonsoul/DragonSoul_Button_03.tga",
						},
						## mall_button
						{
							"name" : "mall_button",
							"type" : "button",

							"x" : 53,
							"y" : 186,

							"tooltip_text" : uiScriptLocale.MALL_TITLE,
					
							"default_image" : "d:/ymir work/ui/game/taskbar/Mall_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/taskbar/Mall_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/taskbar/Mall_Button_03.tga",
						},
						## premium_private_shop_button
						{
							"name" : "OPSButton",
							"type" : "button",

							"x" : 91,
							"y" : 186,

							"tooltip_text" : "Pazar",
					
							"default_image" : "icon/item/private_button_01.tga",
							"over_image" : "icon/item/private_button_02.tga",
							"down_image" : "icon/item/private_button_03.tga",
						},
						## costume_button
						{
							"name" : "costume_button",
							"type" : "button",

							"x" : 132,
							"y" : 186,

							"tooltip_text" : uiScriptLocale.COSTUME_TITLE,

							"default_image" : "d:/ymir work/ui/game/taskbar/costume_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/taskbar/costume_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/taskbar/costume_Button_03.tga",
						},
					],
				},
			),
		},
	),
}