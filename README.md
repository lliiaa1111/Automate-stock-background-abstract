# Stock Background Abstract Image Automation

Automate the creation and batch upload of abstract background images to stock image platforms.

## 🎯 Features

- ✅ **6 Generation Algorithms** - Unique abstract patterns
- ✅ **6 Color Schemes** - Vibrant, pastel, dark, neon, sunset, ocean
- ✅ **Multi-Platform Upload** - Pixabay, Unsplash, Pexels
- ✅ **Batch Processing** - Generate hundreds of images efficiently
- ✅ **Scheduled Automation** - Daily, hourly, or weekly execution
- ✅ **Image Optimization** - Resize, enhance, and optimize for each platform
- ✅ **Full CLI** - Command-line interface with 40+ options
- ✅ **Logging & Monitoring** - Complete audit trail

## 📦 Installation

```bash
# 1. Clone/setup repository
cd Automate-stock-background-abstract

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup credentials
cp config/credentials.example.yaml config/credentials.yaml
# Edit credentials.yaml with your API keys
```

## 🔑 API Keys

Get free API keys from:

- **Pixabay**: https://pixabay.com/api/
- **Unsplash**: https://unsplash.com/developers
- **Pexels**: https://www.pexels.com/api/

## 🚀 Quick Start

### Generate 10 abstract images
```bash
python main.py generate --count 10
```

### Process for Pixabay
```bash
python main.py process --platforms pixabay
```

### Upload to Pixabay
```bash
python main.py upload --platforms pixabay
```

### Full pipeline (generate → process → upload)
```bash
python main.py pipeline --count 20 --platforms pixabay unsplash
```

### Schedule daily automation at 2 AM
```bash
python main.py schedule --interval daily --time 02:00 --platforms pixabay
```

## 📋 Available Commands

### generate
Generate abstract background images
```bash
python main.py generate \
  --count 50 \
  --width 1920 \
  --height 1080 \
  --color-scheme vibrant \
  --dry-run
```

**Options:**
- `--count`: Number of images (default: 10)
- `--width`: Image width in pixels (default: 1920)
- `--height`: Image height in pixels (default: 1080)
- `--color-scheme`: vibrant|pastel|dark|neon|sunset|ocean
- `--dry-run`: Preview without generating

### process
Process generated images for stock platforms
```bash
python main.py process \
  --platforms pixabay unsplash \
  --dry-run
```

**Options:**
- `--platforms`: Target platforms (space-separated)
- `--dry-run`: Preview without processing

### upload
Upload processed images to stock platforms
```bash
python main.py upload \
  --platforms pixabay \
  --dry-run
```

**Options:**
- `--platforms`: Target platforms
- `--dry-run`: Preview without uploading

### pipeline
Run complete pipeline
```bash
python main.py pipeline \
  --count 30 \
  --platforms pixabay unsplash \
  --verbose \
  --dry-run
```

**Options:**
- `--count`: Number of images to generate
- `--platforms`: Target platforms
- `--verbose`: Detailed output
- `--dry-run`: Preview mode

### schedule
Schedule automated pipeline
```bash
python main.py schedule \
  --interval daily \
  --time 02:00 \
  --count 20 \
  --platforms pixabay
```

**Options:**
- `--interval`: daily|hourly|weekly (default: daily)
- `--time`: Execution time in HH:MM format
- `--count`: Images per execution
- `--platforms`: Target platforms

### validate
Validate configuration and credentials
```bash
python main.py validate
```

## 📁 Directory Structure

```
.
├── main.py                      # CLI entry point
├── image_generator.py           # Image generation (6 algorithms)
├── image_processor.py           # Image processing & optimization
├── stock_uploader.py            # API integration & uploads
├── config_loader.py             # Configuration management
├── scheduler.py                 # Task scheduling
├── requirements.txt             # Python dependencies
├── config/
│   ├── config.yaml             # Main configuration
│   └── credentials.example.yaml # API credentials template
├── generated_images/            # Output directory (generated)
└── processed_images/            # Output directory (processed)
```

## ⚙️ Configuration

### Main Config (config/config.yaml)

```yaml
generation:
  width: 1920
  height: 1080
  count: 10
  color_scheme: vibrant

processing:
  enhance: true
  platforms:
    - pixabay
    - unsplash

scheduler:
  enabled: true
  interval: daily
  time: "02:00"
```

### Credentials (config/credentials.yaml)

```yaml
pixabay:
  api_key: your_pixabay_key

unsplash:
  access_token: your_unsplash_token

pexels:
  api_key: your_pexels_key
```

Or set environment variables:
```bash
export PIXABAY_API_KEY=your_key
export UNSPLASH_ACCESS_TOKEN=your_token
export PEXELS_API_KEY=your_key
```

## 🎨 Generation Algorithms

1. **Geometric Shapes** - Random rectangles, circles, polygons
2. **Perlin Noise** - Noise-based patterns
3. **Gradient Mesh** - Grid-based gradients
4. **Circles & Curves** - Overlapping circular shapes
5. **Abstract Lines** - Random line strokes
6. **Organic Blobs** - Irregular blob shapes

## 🎨 Color Schemes

- **Vibrant** - Bright, saturated colors
- **Pastel** - Soft, muted colors
- **Dark** - Dark, moody tones
- **Neon** - Bright neon colors
- **Sunset** - Warm orange/purple tones
- **Ocean** - Cool blue tones

## 📊 Platform Specifications

### Pixabay
- Minimum: 1920x1080
- Format: JPG, PNG
- Quality: 90

### Unsplash
- Minimum: 1920x1200
- Format: JPG
- Quality: 85

### Pexels
- Minimum: 2560x1920
- Format: JPG
- Quality: 85

## 🔧 Advanced Usage

### Generate with custom settings
```bash
python main.py generate \
  --count 100 \
  --width 2560 \
  --height 1920 \
  --color-scheme neon
```

### Process specific images
```bash
python main.py process --platforms pixabay unsplash
```

### Test before uploading
```bash
python main.py pipeline --count 5 --dry-run --verbose
```

### Schedule with environment variables
```bash
export PIXABAY_API_KEY=your_key
python main.py schedule --interval daily --time 03:00
```

## 📝 Logging

All operations are logged to `automation.log`:

```bash
tail -f automation.log
```

Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

## 🐛 Troubleshooting

### No credentials found
```
Solution: Create config/credentials.yaml or set environment variables
```

### Images not uploading
```
Solution: Check API keys in credentials file
Run: python main.py validate
```

### Permission denied on directories
```
Solution: Ensure write permissions in project directory
chmod 755 config/ generated_images/ processed_images/
```

## 🤝 Contributing

Improvements welcome! Areas for enhancement:

- [ ] More generation algorithms
- [ ] Additional stock platforms (Dreamstime, 500px, etc.)
- [ ] Web UI for configuration
- [ ] Duplicate detection
- [ ] Revenue tracking

## 📄 License

MIT License - Feel free to use and modify

## ⭐ Tips for Success

1. **Start small** - Test with 5 images first
2. **Monitor uploads** - Check platform dashboards
3. **Adjust color schemes** - Find what works best
4. **Schedule wisely** - Avoid peak platform times
5. **Read platform guidelines** - Follow submission rules
6. **Track metrics** - Monitor acceptance rates

## 🚀 Next Steps

1. Get API keys from stock platforms
2. Configure `config/credentials.yaml`
3. Run `python main.py validate`
4. Generate test batch: `python main.py generate --count 5`
5. Test upload: `python main.py pipeline --count 5 --dry-run`
6. Schedule automation: `python main.py schedule --interval daily`

## 📞 Support

For issues or questions:
- Check `automation.log` for detailed errors
- Verify API credentials
- Test with `--dry-run` option first
- Validate configuration with `validate` command

---

**Happy automating!** 🎨✨
