# arat

self.wndInventory = None

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			self.wndEquip = None

#arat

wndInventory = uiInventory.InventoryWindow()

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			wndEquip = uiEquipmentDialog.EquipmentDialog()

#arat

wndInventory.BindInterfaceClass(self)

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			wndEquip.BindInterfaceClass(self)

#arat

self.wndInventory = wndInventory

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			self.wndEquip = wndEquip

#arat

self.wndInventory.SetItemToolTip(self.tooltipItem)

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			self.wndEquip.SetItemToolTip(self.tooltipItem)

#arat

		if self.wndInventory:
			self.wndInventory.Destroy()

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			if self.wndEquip:
				self.wndEquip.Destroy()

#arat

del self.wndInventory

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			del self.wndEquip

#arat

self.wndInventory.RefreshItemSlot()

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			self.wndEquip.RefreshItemSlot()

#arat

self.wndInventory.Show()

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			self.wndEquip.Show()

#arat

		if self.wndInventory:
			self.wndInventory.Hide()

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			if self.wndEquip:
				self.wndEquip.Hide()

#arat

	def ToggleInventoryWindow(self):

#değiştir

	def ToggleInventoryWindow(self):
		if False == player.IsObserverMode():
			if False == self.wndInventory.IsShow():
				self.wndInventory.Show()
				if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
					self.wndEquip.Show()
				self.wndInventory.SetTop()
				if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
					self.wndEquip.SetTop()
			else:
				self.wndInventory.OverOutItem()
				self.wndInventory.Close()
				if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
					self.wndEquip.Close()

#arat

		if self.wndExpandedTaskBar:
			hideWindows += self.wndExpandedTaskBar,

#altına ekle

		if app.ENABLE_ADDITIONAL_EQUIPMENT_PAGE:
			hideWindows += self.wndEquip,