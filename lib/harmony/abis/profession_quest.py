CONTRACT_ADDRESS = '0xAa9a289ce0565E4D6548e63a441e7C084E6B52F6'
ABI = """
        [
           	{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Paused","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct Quest","name":"quest","type":"tuple"}],"name":"QuestCanceled","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct Quest","name":"quest","type":"tuple"}],"name":"QuestCompleted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"address","name":"rewardItem","type":"address"},{"indexed":false,"internalType":"uint256","name":"itemQuantity","type":"uint256"}],"name":"QuestReward","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint8","name":"profession","type":"uint8"},{"indexed":false,"internalType":"uint16","name":"skillUp","type":"uint16"}],"name":"QuestSkillUp","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaFullAt","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"staminaSpent","type":"uint256"}],"name":"QuestStaminaSpent","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"},{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"indexed":false,"internalType":"struct Quest","name":"quest","type":"tuple"}],"name":"QuestStarted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":false,"internalType":"uint64","name":"xpEarned","type":"uint64"}],"name":"QuestXP","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"questId","type":"uint256"},{"indexed":true,"internalType":"address","name":"player","type":"address"},{"indexed":false,"internalType":"uint256","name":"heroId","type":"uint256"},{"indexed":true,"internalType":"address","name":"reward","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"data","type":"uint256"}],"name":"RewardMinted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"bool","name":"success","type":"bool"},{"indexed":false,"internalType":"uint256","name":"attempt","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"TrainingAttemptDone","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"winCount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"attempts","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"TrainingSuccessRatio","type":"event"},
            {"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"}],"name":"Unpaused","type":"event"},
            {"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"MODERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_questAddress","type":"address"}],"name":"activateQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"activeAccountQuests","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"cancelQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"completeQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint256","name":"_questIndex","type":"uint256"}],"name":"deactivateQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_account","type":"address"}],"name":"getAccountActiveQuests","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"_role","type":"bytes32"}],"name":"getAccountsWithRole","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_heroId","type":"uint256"}],"name":"getCurrentStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"heroId","type":"uint256"}],"name":"getHeroQuest","outputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest","name":"","type":"tuple"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"getQuestContracts","outputs":[{"internalType":"address[]","name":"","type":"address[]"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"getRoleMember","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleMemberCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"heroToQuest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"address","name":"_heroCoreAddress","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"isQuest","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest","name":"_quest","type":"tuple"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint8","name":"_profession","type":"uint8"},{"internalType":"uint16","name":"_skillUp","type":"uint16"}],"name":"logSkillUp","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"components":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"uint256[]","name":"heroes","type":"uint256[]"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"internalType":"struct Quest","name":"_quest","type":"tuple"},{"internalType":"uint256","name":"_heroId","type":"uint256"},{"internalType":"uint64","name":"_xpEarned","type":"uint64"}],"name":"logXp","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"}],"name":"multiCancelQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address[]","name":"_questAddress","type":"address[]"},{"internalType":"uint256[][]","name":"_heroIds","type":"uint256[][]"},{"internalType":"uint8[]","name":"_attempts","type":"uint8[]"},{"internalType":"uint8[]","name":"_level","type":"uint8[]"}],"name":"multiStartQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"questCounter","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"questRewarder","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"quests","outputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"questAddress","type":"address"},{"internalType":"uint8","name":"level","type":"uint8"},{"internalType":"address","name":"player","type":"address"},{"internalType":"uint256","name":"startBlock","type":"uint256"},{"internalType":"uint256","name":"startAtTime","type":"uint256"},{"internalType":"uint256","name":"completeAtTime","type":"uint256"},{"internalType":"uint8","name":"attempts","type":"uint8"},{"internalType":"enum QuestStatus","name":"status","type":"uint8"}],"stateMutability":"view","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"address","name":"_questRewarder","type":"address"}],"name":"setQuestRewarder","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256","name":"_timePerStamina","type":"uint256"}],"name":"setTimePerStamina","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint8","name":"_attempts","type":"uint8"},{"internalType":"uint8","name":"_level","type":"uint8"}],"name":"startQuest","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"timePerStamina","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
            {"inputs":[],"name":"unpause","outputs":[],"stateMutability":"nonpayable","type":"function"},
            {"inputs":[{"internalType":"uint256[]","name":"_heroIds","type":"uint256[]"},{"internalType":"address","name":"_questAddress","type":"address"},{"internalType":"uint8","name":"_attempts","type":"uint8"},{"components":[{"internalType":"uint256","name":"uint1","type":"uint256"},{"internalType":"uint256","name":"uint2","type":"uint256"},{"internalType":"uint256","name":"uint3","type":"uint256"},{"internalType":"uint256","name":"uint4","type":"uint256"},{"internalType":"int256","name":"int1","type":"int256"},{"internalType":"int256","name":"int2","type":"int256"},{"internalType":"string","name":"string1","type":"string"},{"internalType":"string","name":"string2","type":"string"},{"internalType":"address","name":"address1","type":"address"},{"internalType":"address","name":"address2","type":"address"},{"internalType":"address","name":"address3","type":"address"},{"internalType":"address","name":"address4","type":"address"}],"internalType":"struct IQuestTypes.QuestData","name":"_questData","type":"tuple"}],"name":"startQuestWithData","outputs":[],"stateMutability":"nonpayable","type":"function"}
        ]
        """