# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Welcome user, i'm {query.message.from_user.mention}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝗮𝗹𝗹𝗼𝘄 𝘆𝗼𝘂 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝗴𝗿𝗼𝘂𝗽𝘀 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗻𝗲𝘄 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺'𝘀 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁𝘀 !**

💡 **𝗙𝗶𝗻𝗱 𝗼𝘂𝘁 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗕𝗼𝘁'𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗮𝗻𝗱 𝗵𝗼𝘄 𝘁𝗵𝗲𝘆 𝘄𝗼𝗿𝗸 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 𝘁𝗵𝗲 » 📚 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗯𝘂𝘁𝘁𝗼𝗻 !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Thêm Tôi Vào Nhóm ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❓ Hướng Giẫn Sử Dụng", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 Các Lệnh", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 Quyên Góp ", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 Nhóm Âm Nhạc", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Kênh Âm Nhạc", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "📥 Admin Music", url="https://t.me/theKingAdminGroup")
                ],[
                    InlineKeyboardButton(
                        "Liên Hệ", url="https://t.me/theKingAdminGroup"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Xin chào, chào mừng bạn đến với menu trợ giúp !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Cơ bản Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Nâng cao Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Chủ nhân Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Niềm Vui Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 Quay Lại", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 đây là điều cơ bản commands</b>

🎧 [ GROUP VC CMD ]

/play (song name) - phát bài hát từ youtube
/ytp (song name) - phát bài hát trực tiếp từ youtube 
/stream (reply to audio) - phát bài hát bằng tệp âm thanh
/playlist - hiển thị danh sách bài hát trong hàng đợi
/song (song name) - tải bài hát từ youtube
/search (video name) - tìm kiếm video chi tiết từ youtube
/vsong (video name) - tải video từ youtube chi tiết
/lyric - (song name) trình trích xuất lời bài hát
/vk (song name) - tải xuống bài hát từ chế độ nội tuyến

🎧 [ CHANNEL VC CMD ]

/cplay - phát trực tuyến nhạc trên kênh trò chuyện thoại
/cplayer - hiển thị bài hát trong phát trực tuyến
/cpause - tạm dừng phát nhạc trực tuyến
/cresume - tiếp tục phát trực tuyến đã bị tạm dừng
/cskip - bỏ qua phát trực tuyến đến bài hát tiếp theo
/cend - kết thúc phát nhạc trực tuyến
/admincache - làm mới bộ nhớ cache của quản trị viên
/ubjoinc - mời trợ lý tham gia kênh của bạn

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Quay Đầu", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 đây là các lệnh nâng cao</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/cache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Quay Xe", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 đây là lệnh quản trị</b>

/player - hiển thị trạng thái phát nhạc
/pause - tạm dừng phát nhạc
/resume - tiếp tục âm nhạc đã bị tạm dừng
/skip - chuyển sang bài hát tiếp theo
/end - dừng phát nhạc
/userbotjoin - mời trợ lý tham gia vào nhóm của bạn
/auth - người dùng được phép sử dụng bot âm nhạc
/deauth - không được phép sử dụng bot âm nhạc
/control - mở bảng cài đặt trình phát
/delcmd (on | off) - bật / tắt tính năng del cmd
/musicplayer (on / off) - tắt / bật trình phát nhạc in your group

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Quay Xe", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 đây là lệnh sudo</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Quay Xe", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 đây là lệnh của chủ sở hữu</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

📝 note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Quay Xe", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 đây là các lệnh thú vị</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Quay Xe", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ CÁCH SỬ DỤNG BOT NÀY:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Danh sách lệnh", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 ĐÓNG", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 here is the control menu of bot:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ pause music", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ resume music", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ skip music", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ end music", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 del cmd", callback_data="cbdelcmds"
                    )
                ]
            ]
        )
    )



@Client.on_callback_query(filters.regex("cbdelcmds"))
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information:</b>
        
**💡 Feature:** delete every commands sent by users to avoid spam in groups !

**❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 QUAY XE", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Căn bản Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Nâng cao Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Chủ nhân Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Niềm vui Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 Quay Xe", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
